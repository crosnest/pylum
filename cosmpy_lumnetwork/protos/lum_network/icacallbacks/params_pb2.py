# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/icacallbacks/params.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lum-network/icacallbacks/params.proto',
  package='lum.network.icacallbacks',
  syntax='proto3',
  serialized_pb=_b('\n%lum-network/icacallbacks/params.proto\x12\x18lum.network.icacallbacks\x1a\x14gogoproto/gogo.proto\"\x0e\n\x06Params:\x04\x98\xa0\x1f\x00\x42\x33Z1github.com/lum-network/chain/x/icacallbacks/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='lum.network.icacallbacks.Params',
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
  DESCRIPTOR = _PARAMS,
  __module__ = 'lum_network.icacallbacks.params_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.icacallbacks.Params)
  ))
_sym_db.RegisterMessage(Params)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z1github.com/lum-network/chain/x/icacallbacks/types'))
_PARAMS.has_options = True
_PARAMS._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000'))
# @@protoc_insertion_point(module_scope)
