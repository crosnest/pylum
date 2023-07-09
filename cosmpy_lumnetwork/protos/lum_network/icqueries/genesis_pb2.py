# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/icqueries/genesis.proto

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
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lum-network/icqueries/genesis.proto',
  package='stride.interchainquery.v1',
  syntax='proto3',
  serialized_pb=_b('\n#lum-network/icqueries/genesis.proto\x12\x19stride.interchainquery.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xab\x01\n\x05Query\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rconnection_id\x18\x02 \x01(\t\x12\x10\n\x08\x63hain_id\x18\x03 \x01(\t\x12\x12\n\nquery_type\x18\x04 \x01(\t\x12\x0f\n\x07request\x18\x05 \x01(\x0c\x12\x13\n\x0b\x63\x61llback_id\x18\x08 \x01(\t\x12\x0b\n\x03ttl\x18\t \x01(\x04\x12\x14\n\x0crequest_sent\x18\x0b \x01(\x08\x12\x10\n\x08\x65xtra_id\x18\x0c \x01(\t\"\xe5\x01\n\tDataPoint\x12\n\n\x02id\x18\x01 \x01(\t\x12S\n\rremote_height\x18\x02 \x01(\tB<\xd2\xb4-\ncosmos.Int\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12R\n\x0clocal_height\x18\x03 \x01(\tB<\xd2\xb4-\ncosmos.Int\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12#\n\x05value\x18\x04 \x01(\x0c\x42\x14\xea\xde\x1f\x10result,omitempty\"G\n\x0cGenesisState\x12\x37\n\x07queries\x18\x01 \x03(\x0b\x32 .stride.interchainquery.v1.QueryB\x04\xc8\xde\x1f\x00\x42\x30Z.github.com/lum-network/chain/x/icqueries/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='stride.interchainquery.v1.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stride.interchainquery.v1.Query.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='stride.interchainquery.v1.Query.connection_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='stride.interchainquery.v1.Query.chain_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query_type', full_name='stride.interchainquery.v1.Query.query_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request', full_name='stride.interchainquery.v1.Query.request', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback_id', full_name='stride.interchainquery.v1.Query.callback_id', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='stride.interchainquery.v1.Query.ttl', index=6,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_sent', full_name='stride.interchainquery.v1.Query.request_sent', index=7,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_id', full_name='stride.interchainquery.v1.Query.extra_id', index=8,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=116,
  serialized_end=287,
)


_DATAPOINT = _descriptor.Descriptor(
  name='DataPoint',
  full_name='stride.interchainquery.v1.DataPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stride.interchainquery.v1.DataPoint.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_height', full_name='stride.interchainquery.v1.DataPoint.remote_height', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Int\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_height', full_name='stride.interchainquery.v1.DataPoint.local_height', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Int\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='stride.interchainquery.v1.DataPoint.value', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\020result,omitempty')), file=DESCRIPTOR),
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
  serialized_start=290,
  serialized_end=519,
)


_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='stride.interchainquery.v1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queries', full_name='stride.interchainquery.v1.GenesisState.queries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=521,
  serialized_end=592,
)

_GENESISSTATE.fields_by_name['queries'].message_type = _QUERY
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['DataPoint'] = _DATAPOINT
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(
  DESCRIPTOR = _QUERY,
  __module__ = 'lum_network.icqueries.genesis_pb2'
  # @@protoc_insertion_point(class_scope:stride.interchainquery.v1.Query)
  ))
_sym_db.RegisterMessage(Query)

DataPoint = _reflection.GeneratedProtocolMessageType('DataPoint', (_message.Message,), dict(
  DESCRIPTOR = _DATAPOINT,
  __module__ = 'lum_network.icqueries.genesis_pb2'
  # @@protoc_insertion_point(class_scope:stride.interchainquery.v1.DataPoint)
  ))
_sym_db.RegisterMessage(DataPoint)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), dict(
  DESCRIPTOR = _GENESISSTATE,
  __module__ = 'lum_network.icqueries.genesis_pb2'
  # @@protoc_insertion_point(class_scope:stride.interchainquery.v1.GenesisState)
  ))
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z.github.com/lum-network/chain/x/icqueries/types'))
_DATAPOINT.fields_by_name['remote_height'].has_options = True
_DATAPOINT.fields_by_name['remote_height']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Int\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'))
_DATAPOINT.fields_by_name['local_height'].has_options = True
_DATAPOINT.fields_by_name['local_height']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\ncosmos.Int\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'))
_DATAPOINT.fields_by_name['value'].has_options = True
_DATAPOINT.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\020result,omitempty'))
_GENESISSTATE.fields_by_name['queries'].has_options = True
_GENESISSTATE.fields_by_name['queries']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
