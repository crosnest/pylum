# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/interchain_accounts/host/v1/query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ibc.applications.interchain_accounts.host.v1 import host_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/applications/interchain_accounts/host/v1/query.proto',
  package='ibc.applications.interchain_accounts.host.v1',
  syntax='proto3',
  serialized_pb=_b('\n8ibc/applications/interchain_accounts/host/v1/query.proto\x12,ibc.applications.interchain_accounts.host.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x37ibc/applications/interchain_accounts/host/v1/host.proto\"\x14\n\x12QueryParamsRequest\"[\n\x13QueryParamsResponse\x12\x44\n\x06params\x18\x01 \x01(\x0b\x32\x34.ibc.applications.interchain_accounts.host.v1.Params2\xcd\x01\n\x05Query\x12\xc3\x01\n\x06Params\x12@.ibc.applications.interchain_accounts.host.v1.QueryParamsRequest\x1a\x41.ibc.applications.interchain_accounts.host.v1.QueryParamsResponse\"4\x82\xd3\xe4\x93\x02.\x12,/ibc/apps/interchain_accounts/host/v1/paramsBLZJgithub.com/cosmos/ibc-go/v5/modules/apps/27-interchain-accounts/host/typesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2.DESCRIPTOR,])




_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='ibc.applications.interchain_accounts.host.v1.QueryParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=193,
  serialized_end=213,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='ibc.applications.interchain_accounts.host.v1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='ibc.applications.interchain_accounts.host.v1.QueryParamsResponse.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=215,
  serialized_end=306,
)

_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2._PARAMS
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYPARAMSREQUEST,
  __module__ = 'ibc.applications.interchain_accounts.host.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.interchain_accounts.host.v1.QueryParamsRequest)
  ))
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYPARAMSRESPONSE,
  __module__ = 'ibc.applications.interchain_accounts.host.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.interchain_accounts.host.v1.QueryParamsResponse)
  ))
_sym_db.RegisterMessage(QueryParamsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('ZJgithub.com/cosmos/ibc-go/v5/modules/apps/27-interchain-accounts/host/types'))

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='ibc.applications.interchain_accounts.host.v1.Query',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=309,
  serialized_end=514,
  methods=[
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='ibc.applications.interchain_accounts.host.v1.Query.Params',
    index=0,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002.\022,/ibc/apps/interchain_accounts/host/v1/params')),
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
