# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/auth/v1beta1/genesis.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/auth/v1beta1/genesis.proto',
  package='cosmos.auth.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n!cosmos/auth/v1beta1/genesis.proto\x12\x13\x63osmos.auth.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/auth/v1beta1/auth.proto\"i\n\x0cGenesisState\x12\x31\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.auth.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12&\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32\x14.google.protobuf.AnyB+Z)github.com/cosmos/cosmos-sdk/x/auth/typesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_auth_dot_v1beta1_dot_auth__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.auth.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='cosmos.auth.v1beta1.GenesisState.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accounts', full_name='cosmos.auth.v1beta1.GenesisState.accounts', index=1,
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
  serialized_start=139,
  serialized_end=244,
)

_GENESISSTATE.fields_by_name['params'].message_type = cosmos_dot_auth_dot_v1beta1_dot_auth__pb2._PARAMS
_GENESISSTATE.fields_by_name['accounts'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), dict(
  DESCRIPTOR = _GENESISSTATE,
  __module__ = 'cosmos.auth.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.GenesisState)
  ))
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/cosmos/cosmos-sdk/x/auth/types'))
_GENESISSTATE.fields_by_name['params'].has_options = True
_GENESISSTATE.fields_by_name['params']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
