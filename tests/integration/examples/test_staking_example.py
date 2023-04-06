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

"""Staking example test."""

import subprocess  # nosec
from pathlib import Path

import pytest


MAX_FLAKY_RERUNS = 3
RERUNS_DELAY = 10

ROOT_DIR = Path(__file__).parent.parent.parent.parent


@pytest.mark.skip
@pytest.mark.integration
@pytest.mark.flaky(reruns=MAX_FLAKY_RERUNS, reruns_delay=RERUNS_DELAY)
def test_staking_example():
    """
    Test examples/aerial_staking.py
    This test need 2 validators running to be successful.
    """
    proc = subprocess.run(  # nosec
        f"python {ROOT_DIR}/examples/aerial_staking.py",
        shell=True,
        check=True,
        capture_output=True,
        timeout=100,
    )

    assert b"Summary: Staked: 15" in proc.stdout, proc.stdout
