# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/beam/genesis.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from lum_network.beam import beam_pb2 as lum__network_dot_beam_dot_beam__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lum-network/beam/genesis.proto',
  package='lum.network.beam',
  syntax='proto3',
  serialized_pb=_b('\n\x1elum-network/beam/genesis.proto\x12\x10lum.network.beam\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1blum-network/beam/beam.proto\"\x97\x01\n\x0cGenesisState\x12`\n\x16module_account_balance\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB%\xf2\xde\x1f\x1dyaml:\"module_account_balance\"\xc8\xde\x1f\x00\x12%\n\x05\x62\x65\x61ms\x18\x02 \x03(\x0b\x32\x16.lum.network.beam.BeamB+Z)github.com/lum-network/chain/x/beam/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,lum__network_dot_beam_dot_beam__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='lum.network.beam.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='module_account_balance', full_name='lum.network.beam.GenesisState.module_account_balance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\035yaml:\"module_account_balance\"\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beams', full_name='lum.network.beam.GenesisState.beams', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=287,
)

_GENESISSTATE.fields_by_name['module_account_balance'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_GENESISSTATE.fields_by_name['beams'].message_type = lum__network_dot_beam_dot_beam__pb2._BEAM
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), dict(
  DESCRIPTOR = _GENESISSTATE,
  __module__ = 'lum_network.beam.genesis_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.beam.GenesisState)
  ))
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/lum-network/chain/x/beam/types'))
_GENESISSTATE.fields_by_name['module_account_balance'].has_options = True
_GENESISSTATE.fields_by_name['module_account_balance']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\035yaml:\"module_account_balance\"\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
