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
"""This module contains the tests for the aerial/tx_helpers module."""
from unittest.mock import Mock, patch

import pytest

from pylum.aerial.client import LedgerClient
from pylum.aerial.config import NetworkConfig
from pylum.aerial.exceptions import NotFoundError, QueryTimeoutError
from pylum.aerial.tx_helpers import SubmittedTx


def test_broadcast_tx_timeouts():
    """Test for SubmittedTx.wait_to_complete."""
    client = LedgerClient(NetworkConfig.chain4energy_stable_testnet())
    tx = SubmittedTx(client, Mock())
    poll_period = 0.1

    with patch.object(client, "query_tx", side_effect=NotFoundError), patch(
        "time.sleep"
    ) as time_sleep:
        with pytest.raises(QueryTimeoutError):
            tx.wait_to_complete(timeout=0.1, poll_period=0.1)
    time_sleep.assert_called_with(poll_period)

    with patch.object(
        client, "query_tx", side_effect=[NotFoundError, NotFoundError, Mock()]
    ):
        with pytest.raises(QueryTimeoutError):
            tx.wait_to_complete(timeout=0.1, poll_period=0.2)
