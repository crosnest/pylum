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

"""Tests for the Address module of the Crypto Package."""

import json
import unittest

from cosmpy_chain4energy.common.utils import json_encode
from cosmpy_chain4energy.crypto.address import Address
from cosmpy_chain4energy.crypto.keypairs import PublicKey


class AddressTestCase(unittest.TestCase):
    """Test case of KeyPair module."""

    def test_create_from_public_key(self):
        """Test create Address from public key with positive result."""
        pk = PublicKey(
            b"\x02W\xbe\xe2\x08\xdc\x80(\xd2\xd0C\xbe\xe0{\x02\x81\xa6\xf9Y\x19\x0e\xd1\x8a*\x99\x84\xd6e\x07\x99\x8d\x96h"
        )
        address = Address(pk)
        self.assertEqual(str(address), "c4e12hyw0z8za0sc9wwfhkdz2qrc89a87z423p6ch6")
        self.assertEqual(address, "c4e12hyw0z8za0sc9wwfhkdz2qrc89a87z423p6ch6")
        self.assertEqual(
            bytes(address),
            b"U\xc8\xe7\x88\xe2\xeb\xe1\x82\xb9\xc9\xbd\x9a%\x00x9z\x7f\n\xaa",
        )

    def test_create_from_address(self):
        """Test create Address from another Address with positive result."""
        addr1 = Address(
            b"U\xc8\xe7\x88\xe2\xeb\xe1\x82\xb9\xc9\xbd\x9a%\x00x9z\x7f\n\xaa"
        )
        addr2 = Address(addr1)
        self.assertEqual(str(addr1), str(addr2))

    def test_create_from_bytes(self):
        """Test create Address from bytes with positive result."""
        address = Address(
            b"U\xc8\xe7\x88\xe2\xeb\xe1\x82\xb9\xc9\xbd\x9a%\x00x9z\x7f\n\xaa"
        )
        self.assertEqual(str(address), "c4e12hyw0z8za0sc9wwfhkdz2qrc89a87z423p6ch6")

    def test_create_from_str(self):
        """Test create Address from string with positive result."""
        address = Address("c4e12hyw0z8za0sc9wwfhkdz2qrc89a87z423p6ch6")
        self.assertEqual(
            bytes(address),
            b"U\xc8\xe7\x88\xe2\xeb\xe1\x82\xb9\xc9\xbd\x9a%\x00x9z\x7f\n\xaa",
        )

    def test_invalid_byte_length_address(self):
        """Test create Address from bytes with negative result."""
        with self.assertRaises(RuntimeError):
            Address(b"wrong byte len")

    def test_invalid_bech32_address(self):
        """Test create Address from str with negative result."""
        with self.assertRaises(RuntimeError):
            Address("certainly not an address")

    def test_address_from_address_with_custom_prefix(self):
        """Test create an Address from another but with a custom prefix."""
        address = Address("c4e1t62t32vvkr78zdws3jvu9rxjkz3fy0ex4v7e7l")
        val_address = Address(address, prefix="c4evaloper")
        self.assertEqual(
            str(val_address), "fetchvaloper12hyw0z8za0sc9wwfhkdz2qrc89a87z42yq4jl5"
        )

    def test_string_compatible_address(self):
        """Test address can be dumped to json using json_encode utility method."""
        address = Address("c4e1t62t32vvkr78zdws3jvu9rxjkz3fy0ex4v7e7l")
        json_data = json_encode({"address": address})
        restored_address = Address(json.loads(json_data)["address"])
        assert restored_address == address
