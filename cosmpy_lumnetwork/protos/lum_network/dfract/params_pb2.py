# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/dfract/params.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lum-network/dfract/params.proto',
  package='lum.network.dfract',
  syntax='proto3',
  serialized_pb=_b('\n\x1flum-network/dfract/params.proto\x12\x12lum.network.dfract\"<\n\x06Params\x12\x16\n\x0e\x64\x65posit_denoms\x18\x01 \x03(\t\x12\x1a\n\x12min_deposit_amount\x18\x02 \x01(\rB-Z+github.com/lum-network/chain/x/dfract/typesb\x06proto3')
)




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='lum.network.dfract.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deposit_denoms', full_name='lum.network.dfract.Params.deposit_denoms', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_deposit_amount', full_name='lum.network.dfract.Params.min_deposit_amount', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=55,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
  DESCRIPTOR = _PARAMS,
  __module__ = 'lum_network.dfract.params_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.dfract.Params)
  ))
_sym_db.RegisterMessage(Params)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z+github.com/lum-network/chain/x/dfract/types'))
# @@protoc_insertion_point(module_scope)
