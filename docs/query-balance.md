A  [`LedgerClient`](connect-to-network.md) object can be used to query the balances associated with a particular address:

```python
address: str = 'c4e1t62t32vvkr78zdws3jvu9rxjkz3fy0ex4v7e7l'
balances = ledger_client.query_bank_all_balances(address)
```

This will return a `List` of `Coin` objects that contain `amount` and  `denom` variables that correspond to all the funds held at the address and their denominations. This list includes all natively defined coins along with any tokens transferred using the inter-blockchain communication ([IBC](https://ibcprotocol.dev/)) protocol.

```python
>>> balances
[Coin(amount='29263221445595384075', denom='afet')]
```

It's also possible to query the funds associated with a particular denomination by calling  

```python
balance = ledger_client.query_bank_balance(address, denom='afet')
```

which will return the value of the (integer) funds held by the address with the specified denomination. If the `denom` argument is omitted the function will return the fee denomination specified in the `NetworkConfig` object used to initialise the `LedgerClient`.
