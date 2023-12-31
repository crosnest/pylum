# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/genesis.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ibc.applications.transfer.v1 import transfer_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/applications/transfer/v1/genesis.proto',
  package='ibc.applications.transfer.v1',
  syntax='proto3',
  serialized_pb=_b('\n*ibc/applications/transfer/v1/genesis.proto\x12\x1cibc.applications.transfer.v1\x1a+ibc/applications/transfer/v1/transfer.proto\x1a\x14gogoproto/gogo.proto\"\xd6\x01\n\x0cGenesisState\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12\x65\n\x0c\x64\x65nom_traces\x18\x02 \x03(\x0b\x32(.ibc.applications.transfer.v1.DenomTraceB%\xaa\xdf\x1f\x06Traces\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:\"denom_traces\"\x12:\n\x06params\x18\x03 \x01(\x0b\x32$.ibc.applications.transfer.v1.ParamsB\x04\xc8\xde\x1f\x00\x42\x39Z7github.com/cosmos/ibc-go/v5/modules/apps/transfer/typesb\x06proto3')
  ,
  dependencies=[ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='ibc.applications.transfer.v1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_id', full_name='ibc.applications.transfer.v1.GenesisState.port_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\016yaml:\"port_id\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denom_traces', full_name='ibc.applications.transfer.v1.GenesisState.denom_traces', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\006Traces\310\336\037\000\362\336\037\023yaml:\"denom_traces\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='ibc.applications.transfer.v1.GenesisState.params', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=144,
  serialized_end=358,
)

_GENESISSTATE.fields_by_name['denom_traces'].message_type = ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2._DENOMTRACE
_GENESISSTATE.fields_by_name['params'].message_type = ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2._PARAMS
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), dict(
  DESCRIPTOR = _GENESISSTATE,
  __module__ = 'ibc.applications.transfer.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.GenesisState)
  ))
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z7github.com/cosmos/ibc-go/v5/modules/apps/transfer/types'))
_GENESISSTATE.fields_by_name['port_id'].has_options = True
_GENESISSTATE.fields_by_name['port_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\016yaml:\"port_id\"'))
_GENESISSTATE.fields_by_name['denom_traces'].has_options = True
_GENESISSTATE.fields_by_name['denom_traces']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\006Traces\310\336\037\000\362\336\037\023yaml:\"denom_traces\"'))
_GENESISSTATE.fields_by_name['params'].has_options = True
_GENESISSTATE.fields_by_name['params']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
