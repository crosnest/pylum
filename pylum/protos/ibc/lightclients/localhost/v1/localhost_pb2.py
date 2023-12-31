# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/lightclients/localhost/v1/localhost.proto

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
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/lightclients/localhost/v1/localhost.proto',
  package='ibc.lightclients.localhost.v1',
  syntax='proto3',
  serialized_pb=_b('\n-ibc/lightclients/localhost/v1/localhost.proto\x12\x1dibc.lightclients.localhost.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fibc/core/client/v1/client.proto\"l\n\x0b\x43lientState\x12%\n\x08\x63hain_id\x18\x01 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:\"chain_id\"\x12\x30\n\x06height\x18\x02 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00:\x04\x88\xa0\x1f\x00\x42\x46ZDgithub.com/cosmos/ibc-go/v5/modules/light-clients/09-localhost/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,ibc_dot_core_dot_client_dot_v1_dot_client__pb2.DESCRIPTOR,])




_CLIENTSTATE = _descriptor.Descriptor(
  name='ClientState',
  full_name='ibc.lightclients.localhost.v1.ClientState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='ibc.lightclients.localhost.v1.ClientState.chain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\017yaml:\"chain_id\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='ibc.lightclients.localhost.v1.ClientState.height', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=243,
)

_CLIENTSTATE.fields_by_name['height'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
DESCRIPTOR.message_types_by_name['ClientState'] = _CLIENTSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientState = _reflection.GeneratedProtocolMessageType('ClientState', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTSTATE,
  __module__ = 'ibc.lightclients.localhost.v1.localhost_pb2'
  # @@protoc_insertion_point(class_scope:ibc.lightclients.localhost.v1.ClientState)
  ))
_sym_db.RegisterMessage(ClientState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('ZDgithub.com/cosmos/ibc-go/v5/modules/light-clients/09-localhost/types'))
_CLIENTSTATE.fields_by_name['chain_id'].has_options = True
_CLIENTSTATE.fields_by_name['chain_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\017yaml:\"chain_id\"'))
_CLIENTSTATE.fields_by_name['height'].has_options = True
_CLIENTSTATE.fields_by_name['height']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_CLIENTSTATE.has_options = True
_CLIENTSTATE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000'))
# @@protoc_insertion_point(module_scope)
