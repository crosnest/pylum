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
"""Integration tests for basic transactions."""
from typing import Optional

import pytest

from pylum.aerial.client import LedgerClient
from pylum.aerial.config import NetworkConfig
from pylum.aerial.faucet import FaucetApi
from pylum.aerial.wallet import LocalWallet


MAX_FLAKY_RERUNS = 3
RERUNS_DELAY = 10


class TestTx:
    """Test Basic Transaction"""

    COIN = "uc4e"
    GAS_LIMIT: Optional[int] = None

    def _get_network_config(self):
        """Get network config."""
        return NetworkConfig.chain4energy_integration_testnet()

    def get_ledger(self):
        """Get Ledger"""
        return LedgerClient(self._get_network_config())

    def get_wallet_1(self):
        """Get wallet 1."""
        faucet_api = FaucetApi(self._get_network_config())
        wallet1 = LocalWallet.generate()
        faucet_api.get_wealth(wallet1.address(), "100000000uc4e")
        return wallet1

    def get_wallet_2(self):
        """Get wallet 2."""
        wallet2 = LocalWallet.generate()
        return wallet2

    @pytest.mark.integration
    @pytest.mark.flaky(reruns=MAX_FLAKY_RERUNS, reruns_delay=RERUNS_DELAY)
    def test_faucet_transaction_balance(self):
        """Test faucet claims, tx settled, balance check."""
        ledger = self.get_ledger()
        wallet1 = self.get_wallet_1()
        wallet2 = self.get_wallet_2()

        wallet1_initial_balance = ledger.query_bank_balance(wallet1.address())
        wallet2_balance1 = ledger.query_bank_balance(wallet2.address())
        tokens_to_send = int(10)
        assert wallet1_initial_balance >= tokens_to_send
        tx = ledger.send_tokens(
            wallet2.address(),
            tokens_to_send,
            self.COIN,
            wallet1,
            gas_limit=self.GAS_LIMIT,
        )
        tx.wait_to_complete()
        wallet2_balance2 = ledger.query_bank_balance(wallet2.address())
        assert wallet2_balance2 == wallet2_balance1 + tokens_to_send
        wallet1_balance = ledger.query_bank_balance(wallet1.address())
        assert wallet1_balance < wallet1_initial_balance


class TestTxRestAPI(TestTx):
    """Test c4echain rest api"""

    def _get_network_config(self):
        return NetworkConfig(
            chain_id="c4echain",
            url="rest+http://127.0.0.1:1317",
            fee_minimum_gas_price=0.025,
            fee_denomination="uc4e",
            staking_denomination="uc4e",
            faucet_url="http://127.0.0.1:4500",
        )


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
