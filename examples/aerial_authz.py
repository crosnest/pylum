"""Example of aerial authz: authz_address and authz_wallet."""

# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
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
import argparse
from datetime import datetime, timedelta

from pylum.aerial.client import LedgerClient, NetworkConfig
from pylum.aerial.client.utils import (
    prepare_and_broadcast_basic_transaction,
)
from pylum.aerial.faucet import FaucetApi
from pylum.aerial.tx import Transaction
from pylum.aerial.wallet import LocalWallet
from pylum.protos.cosmos.authz.v1beta1.authz_pb2 import Grant
from pylum.protos.cosmos.authz.v1beta1.tx_pb2 import MsgGrant
from pylum.protos.cosmos.bank.v1beta1.authz_pb2 import SendAuthorization
from pylum.protos.cosmos.base.v1beta1.coin_pb2 import Coin
from google.protobuf import any_pb2, timestamp_pb2


def _parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "authz_address",
        help="address that will be granted authorization to send tokens from wallet",
    )
    parser.add_argument(
        "total_authz_time",
        type=int,
        nargs="?",
        default=10,
        help="authorization time for authz_address in minutes",
    )
    parser.add_argument(
        "spend_limit",
        type=int,
        nargs="?",
        default=1000000000000000000,
        help="maximum tokens that authz_wallet will be able to spend from wallet",
    )

    return parser.parse_args()


def main():
    """Run main."""
    args = _parse_commandline()

    wallet = LocalWallet.generate()

    authz_address = args.authz_address

    ledger = LedgerClient(NetworkConfig.chain4energy_stable_testnet())
    faucet_api = FaucetApi(NetworkConfig.chain4energy_stable_testnet())

    total_authz_time = args.total_authz_time
    wallet_balance = ledger.query_bank_balance(wallet.address())

    amount = args.spend_limit

    while wallet_balance < (amount):
        print("Providing wealth to wallet...")
        faucet_api.get_wealth(wallet.address(), "100000000uc4e")
        wallet_balance = ledger.query_bank_balance(wallet.address())

    spend_amount = Coin(amount=str(amount), denom="uc4e")

    # Authorize authz_wallet to send tokens from wallet
    authz_any = any_pb2.Any()
    authz_any.Pack(
        SendAuthorization(spend_limit=[spend_amount]),
        "",
    )

    expiry = timestamp_pb2.Timestamp()
    expiry.FromDatetime(datetime.now() + timedelta(seconds=total_authz_time * 60))
    grant = Grant(authorization=authz_any, expiration=expiry)

    msg = MsgGrant(
        granter=str(wallet.address()),
        grantee=authz_address,
        grant=grant,
    )

    tx = Transaction()
    tx.add_message(msg)

    tx = prepare_and_broadcast_basic_transaction(ledger, tx, wallet)
    tx.wait_to_complete()


if __name__ == "__main__":
    main()
