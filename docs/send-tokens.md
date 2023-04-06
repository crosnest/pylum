Once you have your [`wallet`](wallets-and-keys.md) configured, you can send transactions to the network. The `LedgerClient` object provides useful utilities to do common operations. The following example shows how to send `10` `atestfet` to another address:

```python
destination_address = 'c4e1t62t32vvkr78zdws3jvu9rxjkz3fy0ex4v7e7l'

tx = ledger_client.send_tokens(destination_address, 10, "atestfet", wallet)

# block until the transaction has been successful or failed
tx.wait_to_complete()
```
