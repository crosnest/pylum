<h1 align="center">
    <b>pyLum</b>
</h1>

<p align="center">
A python library for interacting with LumNetwork blockchain
</p>

<p align="center">
  <a href="https://pypi.org/project/pylum/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/pylum">
  </a>
  <a href="https://pypi.org/project/pylum/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pylum">
  </a>
  <a href="https://github.com/crosnest/pylum/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/pypi/l/pylum">
  </a>
  <br />
  <a>
    <img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/pylum">
  </a>
  <a href="https://github.com/crosnest/pylum/actions/workflows/workflow.yml">
    <img alt="pyLum sanity checks and tests" src="https://github.com/crosnest/pylum/actions/workflows/workflow.yml/badge.svg">
  </a>
  <a href="https://pypi.org/project/pylum/">
    <img alt="Download per Month" src="https://img.shields.io/pypi/dm/pylum">
  </a>
</p>

> We recently stopped using the `develop` branch for feature consolidation and renamed `master` to `main`. Please see the [Contribution Guides][contributing] for up-to-date instructions.

## To Install

```bash
pip3 install pylum
```

## Getting Started

Below is a simple example for querying an account's balances:

```python
from pylum.aerial.client import LedgerClient, NetworkConfig

# connect to Fetch.ai network using default parameters
ledger_client = LedgerClient(NetworkConfig.lumnetwork_mainnet())

alice: str = 'fetch12q5gw9l9d0yyq2th77x6pjsesczpsly8h5089x'
balances = ledger_client.query_bank_all_balances(alice)

# show all coin balances
for coin in balances:
  print(f'{coin.amount}{coin.denom}')
```

## Documentation

The full documentation can be found [here](https://docs.fetch.ai/CosmPy/).

## Examples

Under the `examples` directory, you can find examples of basic ledger interactions using `pylum`, such as transferring tokens, staking, deploying and interacting with a smart contract, and performing atomic swaps.

## Contributing

All contributions are very welcome! Remember, contribution is not only PRs and code, but any help with docs or helping other developers solve their issues are very appreciated!

Read below to learn how you can take part in the pyLum project.

### Code of Conduct

Please be sure to read and follow our [Code of Conduct][coc]. By participating, you are expected to uphold this code.

### Contribution Guidelines

Read our [contribution guidelines][contributing] to learn about our issue and pull request submission processes, coding rules, and more.

### Development Guidelines

Read our [development guidelines][developing] to learn about the development processes and workflows.

### Issues, Questions and Discussions

We use [GitHub Issues][issues] for tracking requests and bugs, and [GitHub Discussions][discussion] for general questions and discussion.

## License

The pyLum project is licensed under [Apache License 2.0][license].

[contributing]: https://github.com/crosnest/pylum/blob/main/CONTRIBUTING.md
[developing]: https://github.com/fetchai/cosmpy/blob/main/DEVELOPING.md
[coc]: https://github.com/fetchai/cosmpy/blob/main/CODE_OF_CONDUCT.md
[discussion]: https://github.com/fetchai/cosmpy/discussions
[issues]: https://github.com/fetchai/cosmpy/issues
[license]: https://github.com/fetchai/cosmpy/blob/main/LICENSE