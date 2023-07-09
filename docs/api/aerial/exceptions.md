<a id="cosmpy_lumnetwork.aerial.exceptions"></a>

# cosmpy`_`chain4energy.aerial.exceptions

Exceptions.

<a id="cosmpy_lumnetwork.aerial.exceptions.QueryError"></a>

## QueryError Objects

```python
class QueryError(RuntimeError)
```

Invalid Query Error.

<a id="cosmpy_lumnetwork.aerial.exceptions.NotFoundError"></a>

## NotFoundError Objects

```python
class NotFoundError(QueryError)
```

Not found Error.

<a id="cosmpy_lumnetwork.aerial.exceptions.QueryTimeoutError"></a>

## QueryTimeoutError Objects

```python
class QueryTimeoutError(QueryError)
```

Query timeout Error.

<a id="cosmpy_lumnetwork.aerial.exceptions.BroadcastError"></a>

## BroadcastError Objects

```python
class BroadcastError(RuntimeError)
```

Broadcast Error.

<a id="cosmpy_lumnetwork.aerial.exceptions.BroadcastError.__init__"></a>

#### `__`init`__`

```python
def __init__(tx_hash: str, message: str)
```

Init Broadcast error.

**Arguments**:

- `tx_hash`: transaction hash
- `message`: message

<a id="cosmpy_lumnetwork.aerial.exceptions.OutOfGasError"></a>

## OutOfGasError Objects

```python
class OutOfGasError(BroadcastError)
```

Insufficient Fess Error.

<a id="cosmpy_lumnetwork.aerial.exceptions.OutOfGasError.__init__"></a>

#### `__`init`__`

```python
def __init__(tx_hash: str, gas_wanted: int, gas_used: int)
```

Initialize.

**Arguments**:

- `tx_hash`: transaction hash
- `gas_wanted`: gas required to complete the transaction
- `gas_used`: gas used

<a id="cosmpy_lumnetwork.aerial.exceptions.InsufficientFeesError"></a>

## InsufficientFeesError Objects

```python
class InsufficientFeesError(BroadcastError)
```

Insufficient Fess Error.

<a id="cosmpy_lumnetwork.aerial.exceptions.InsufficientFeesError.__init__"></a>

#### `__`init`__`

```python
def __init__(tx_hash: str, minimum_required_fee: str)
```

Initialize.

**Arguments**:

- `tx_hash`: transaction hash
- `minimum_required_fee`: Minimum required fee

