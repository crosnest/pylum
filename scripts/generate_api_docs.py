#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This tool generates the API docs."""
import argparse
import re
import shutil
import subprocess  # nosec
import sys
from pathlib import Path


DOCS_DIR = Path("docs/")
API_DIR = DOCS_DIR / "api/"
COSMPY_DIR = Path("pylum")

IGNORE_NAMES = {r"^__version__\.py$", r"^py\.typed$", r"^.*_pb2.py$"}
IGNORE_PREFIXES = {
    Path("pylum", "__init__.py"),
    Path("pylum", "aerial", "__init__.py"),
    Path("pylum", "auth"),
    Path("pylum", "bank"),
    Path("pylum", "common"),
    Path("pylum", "crypto"),
    Path("pylum", "distribution"),
    Path("pylum", "evidence"),
    Path("pylum", "gov"),
    Path("pylum", "ibc"),
    Path("pylum", "params"),
    Path("pylum", "protos"),
    Path("pylum", "slashing"),
    Path("pylum", "staking"),
    Path("pylum", "tendermint"),
    Path("pylum", "tx"),
    Path("pylum", "upgrade"),
    Path("pylum", "whitelist.py"),
}


def create_subdir(path: str) -> None:
    """
    Create a subdirectory.

    :param path: the directory path
    """
    directory = "/".join(path.split("/")[:-1])
    Path(directory).mkdir(parents=True, exist_ok=True)


def replace_underscores(text: str) -> str:
    """
    Replace escaped underscores in a text.

    :param text: the text to replace underscores in
    :return: the processed text
    """
    text_a = text.replace("\\_\\_", "`__`")
    text_b = text_a.replace("\\_", "`_`")
    return text_b


def is_relative_to(p1: Path, p2: Path) -> bool:
    """Check if a path is relative to another path."""
    return str(p1).startswith(str(p2))


def is_not_dir(p: Path) -> bool:
    """Call p.is_dir() method and negate the result."""
    return not p.is_dir()


def should_skip(module_path: Path) -> bool:
    """Return true if the file should be skipped."""
    if any(re.search(pattern, module_path.name) for pattern in IGNORE_NAMES):
        print("Skipping, it's in ignore patterns")
        return True
    if module_path.suffix != ".py":
        print("Skipping, it's not a Python module.")
        return True
    if any(is_relative_to(module_path, prefix) for prefix in IGNORE_PREFIXES):
        print(f"Ignoring prefix {module_path}")
        return True
    return False


def _generate_apidocs_cosmpy_modules() -> None:
    """Generate API docs for pylum.* modules."""
    for module_path in filter(is_not_dir, Path(COSMPY_DIR).rglob("*")):
        print(f"Processing {module_path}... ", end="")
        if should_skip(module_path):
            continue
        parents = module_path.parts[:-1]
        parents_without_root = module_path.parts[1:-1]
        last = module_path.stem
        doc_file = API_DIR / Path(*parents_without_root) / f"{last}.md"
        dotted_path = ".".join(parents) + "." + last
        make_pydoc(dotted_path, doc_file)


def make_pydoc(dotted_path: str, destination_file: Path) -> None:
    """Make a PyDoc file."""
    print(
        f"Running with dotted path={dotted_path} and destination_file={destination_file}... ",
        end="",
    )
    try:
        api_doc_content = run_pydoc_markdown(dotted_path)
        destination_file.parent.mkdir(parents=True, exist_ok=True)
        destination_file.write_text(api_doc_content)
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error: {str(e)}")
        return
    print("Done!")


def run_pydoc_markdown(module: str) -> str:
    """
    Run pydoc-markdown.

    :param module: the dotted path.
    :return: the PyDoc content (pre-processed).
    """
    with subprocess.Popen(
        ["pydoc-markdown", "-m", module, "-I", "."], stdout=subprocess.PIPE
    ) as pydoc:
        stdout, _ = pydoc.communicate()
        pydoc.wait()
        stdout_text = stdout.decode("utf-8")
        text = replace_underscores(stdout_text)
        return text


def generate_api_docs() -> None:
    """Generate the api docs."""
    shutil.rmtree(API_DIR, ignore_errors=True)
    API_DIR.mkdir()
    _generate_apidocs_cosmpy_modules()


def install(package: str) -> int:
    """
    Install a PyPI package by calling pip.

    :param package: the package name and version specifier.
    :return: the return code.
    """
    return subprocess.check_call(  # nosec
        [sys.executable, "-m", "pip", "install", package]
    )


def check_working_tree_is_dirty() -> None:
    """Check if the current Git working tree is dirty."""
    print("Checking whether the Git working tree is dirty...")
    result = subprocess.check_output(["git", "diff", "--stat"])  # nosec
    if len(result) > 0:
        print("Git working tree is dirty:")
        print(result.decode("utf-8"))
        sys.exit(1)
    else:
        print("All good!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("generate_api_docs")
    parser.add_argument(
        "--check-clean", action="store_true", help="Check if the working tree is clean."
    )
    arguments = parser.parse_args()

    res = shutil.which("pydoc-markdown")
    if res is None:
        install("pydoc-markdown==4.6.3")
        sys.exit(1)

    generate_api_docs()

    if arguments.check_clean:
        check_working_tree_is_dirty()
