# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/tx.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos.authz.v1beta1 import authz_pb2 as cosmos_dot_authz_dot_v1beta1_dot_authz__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/authz/v1beta1/tx.proto',
  package='cosmos.authz.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\x1d\x63osmos/authz/v1beta1/tx.proto\x12\x14\x63osmos.authz.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a cosmos/authz/v1beta1/authz.proto\x1a\x17\x63osmos/msg/v1/msg.proto\"\xa0\x01\n\x08MsgGrant\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x30\n\x05grant\x18\x03 \x01(\x0b\x32\x1b.cosmos.authz.v1beta1.GrantB\x04\xc8\xde\x1f\x00:\x0c\x82\xe7\xb0*\x07granter\"\"\n\x0fMsgExecResponse\x12\x0f\n\x07results\x18\x01 \x03(\x0c\"\x88\x01\n\x07MsgExec\x12)\n\x07grantee\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x44\n\x04msgs\x18\x02 \x03(\x0b\x32\x14.google.protobuf.AnyB \xca\xb4-\x1csdk.Msg, authz.Authorization:\x0c\x82\xe7\xb0*\x07grantee\"\x12\n\x10MsgGrantResponse\"\x85\x01\n\tMsgRevoke\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x14\n\x0cmsg_type_url\x18\x03 \x01(\t:\x0c\x82\xe7\xb0*\x07granter\"\x13\n\x11MsgRevokeResponse2\xf8\x01\n\x03Msg\x12O\n\x05Grant\x12\x1e.cosmos.authz.v1beta1.MsgGrant\x1a&.cosmos.authz.v1beta1.MsgGrantResponse\x12L\n\x04\x45xec\x12\x1d.cosmos.authz.v1beta1.MsgExec\x1a%.cosmos.authz.v1beta1.MsgExecResponse\x12R\n\x06Revoke\x12\x1f.cosmos.authz.v1beta1.MsgRevoke\x1a\'.cosmos.authz.v1beta1.MsgRevokeResponseB*Z$github.com/cosmos/cosmos-sdk/x/authz\xc8\xe1\x1e\x00\x62\x06proto3')
  ,
  dependencies=[cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,cosmos_dot_authz_dot_v1beta1_dot_authz__pb2.DESCRIPTOR,cosmos_dot_msg_dot_v1_dot_msg__pb2.DESCRIPTOR,])




_MSGGRANT = _descriptor.Descriptor(
  name='MsgGrant',
  full_name='cosmos.authz.v1beta1.MsgGrant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.authz.v1beta1.MsgGrant.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.authz.v1beta1.MsgGrant.grantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grant', full_name='cosmos.authz.v1beta1.MsgGrant.grant', index=2,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\007granter')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=351,
)


_MSGEXECRESPONSE = _descriptor.Descriptor(
  name='MsgExecResponse',
  full_name='cosmos.authz.v1beta1.MsgExecResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='cosmos.authz.v1beta1.MsgExecResponse.results', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=353,
  serialized_end=387,
)


_MSGEXEC = _descriptor.Descriptor(
  name='MsgExec',
  full_name='cosmos.authz.v1beta1.MsgExec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.authz.v1beta1.MsgExec.grantee', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgs', full_name='cosmos.authz.v1beta1.MsgExec.msgs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\264-\034sdk.Msg, authz.Authorization')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\007grantee')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=526,
)


_MSGGRANTRESPONSE = _descriptor.Descriptor(
  name='MsgGrantResponse',
  full_name='cosmos.authz.v1beta1.MsgGrantResponse',
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
  serialized_start=528,
  serialized_end=546,
)


_MSGREVOKE = _descriptor.Descriptor(
  name='MsgRevoke',
  full_name='cosmos.authz.v1beta1.MsgRevoke',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.authz.v1beta1.MsgRevoke.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.authz.v1beta1.MsgRevoke.grantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_type_url', full_name='cosmos.authz.v1beta1.MsgRevoke.msg_type_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\007granter')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=549,
  serialized_end=682,
)


_MSGREVOKERESPONSE = _descriptor.Descriptor(
  name='MsgRevokeResponse',
  full_name='cosmos.authz.v1beta1.MsgRevokeResponse',
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
  serialized_start=684,
  serialized_end=703,
)

_MSGGRANT.fields_by_name['grant'].message_type = cosmos_dot_authz_dot_v1beta1_dot_authz__pb2._GRANT
_MSGEXEC.fields_by_name['msgs'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['MsgGrant'] = _MSGGRANT
DESCRIPTOR.message_types_by_name['MsgExecResponse'] = _MSGEXECRESPONSE
DESCRIPTOR.message_types_by_name['MsgExec'] = _MSGEXEC
DESCRIPTOR.message_types_by_name['MsgGrantResponse'] = _MSGGRANTRESPONSE
DESCRIPTOR.message_types_by_name['MsgRevoke'] = _MSGREVOKE
DESCRIPTOR.message_types_by_name['MsgRevokeResponse'] = _MSGREVOKERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgGrant = _reflection.GeneratedProtocolMessageType('MsgGrant', (_message.Message,), dict(
  DESCRIPTOR = _MSGGRANT,
  __module__ = 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgGrant)
  ))
_sym_db.RegisterMessage(MsgGrant)

MsgExecResponse = _reflection.GeneratedProtocolMessageType('MsgExecResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGEXECRESPONSE,
  __module__ = 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgExecResponse)
  ))
_sym_db.RegisterMessage(MsgExecResponse)

MsgExec = _reflection.GeneratedProtocolMessageType('MsgExec', (_message.Message,), dict(
  DESCRIPTOR = _MSGEXEC,
  __module__ = 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgExec)
  ))
_sym_db.RegisterMessage(MsgExec)

MsgGrantResponse = _reflection.GeneratedProtocolMessageType('MsgGrantResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGGRANTRESPONSE,
  __module__ = 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgGrantResponse)
  ))
_sym_db.RegisterMessage(MsgGrantResponse)

MsgRevoke = _reflection.GeneratedProtocolMessageType('MsgRevoke', (_message.Message,), dict(
  DESCRIPTOR = _MSGREVOKE,
  __module__ = 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgRevoke)
  ))
_sym_db.RegisterMessage(MsgRevoke)

MsgRevokeResponse = _reflection.GeneratedProtocolMessageType('MsgRevokeResponse', (_message.Message,), dict(
  DESCRIPTOR = _MSGREVOKERESPONSE,
  __module__ = 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgRevokeResponse)
  ))
_sym_db.RegisterMessage(MsgRevokeResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z$github.com/cosmos/cosmos-sdk/x/authz\310\341\036\000'))
_MSGGRANT.fields_by_name['granter'].has_options = True
_MSGGRANT.fields_by_name['granter']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGGRANT.fields_by_name['grantee'].has_options = True
_MSGGRANT.fields_by_name['grantee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGGRANT.fields_by_name['grant'].has_options = True
_MSGGRANT.fields_by_name['grant']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_MSGGRANT.has_options = True
_MSGGRANT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\007granter'))
_MSGEXEC.fields_by_name['grantee'].has_options = True
_MSGEXEC.fields_by_name['grantee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGEXEC.fields_by_name['msgs'].has_options = True
_MSGEXEC.fields_by_name['msgs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\264-\034sdk.Msg, authz.Authorization'))
_MSGEXEC.has_options = True
_MSGEXEC._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\007grantee'))
_MSGREVOKE.fields_by_name['granter'].has_options = True
_MSGREVOKE.fields_by_name['granter']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGREVOKE.fields_by_name['grantee'].has_options = True
_MSGREVOKE.fields_by_name['grantee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_MSGREVOKE.has_options = True
_MSGREVOKE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\202\347\260*\007granter'))

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='cosmos.authz.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=706,
  serialized_end=954,
  methods=[
  _descriptor.MethodDescriptor(
    name='Grant',
    full_name='cosmos.authz.v1beta1.Msg.Grant',
    index=0,
    containing_service=None,
    input_type=_MSGGRANT,
    output_type=_MSGGRANTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Exec',
    full_name='cosmos.authz.v1beta1.Msg.Exec',
    index=1,
    containing_service=None,
    input_type=_MSGEXEC,
    output_type=_MSGEXECRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Revoke',
    full_name='cosmos.authz.v1beta1.Msg.Revoke',
    index=2,
    containing_service=None,
    input_type=_MSGREVOKE,
    output_type=_MSGREVOKERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
