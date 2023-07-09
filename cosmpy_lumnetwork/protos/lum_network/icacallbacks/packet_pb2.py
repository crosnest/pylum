# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/icacallbacks/packet.proto

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
  name='lum-network/icacallbacks/packet.proto',
  package='lum.network.icacallbacks',
  syntax='proto3',
  serialized_pb=_b('\n%lum-network/icacallbacks/packet.proto\x12\x18lum.network.icacallbacks\"W\n\x16IcacallbacksPacketData\x12\x33\n\x07no_data\x18\x01 \x01(\x0b\x32 .lum.network.icacallbacks.NoDataH\x00\x42\x08\n\x06packet\"\x08\n\x06NoDataB3Z1github.com/lum-network/chain/x/icacallbacks/typesb\x06proto3')
)




_ICACALLBACKSPACKETDATA = _descriptor.Descriptor(
  name='IcacallbacksPacketData',
  full_name='lum.network.icacallbacks.IcacallbacksPacketData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='no_data', full_name='lum.network.icacallbacks.IcacallbacksPacketData.no_data', index=0,
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
    _descriptor.OneofDescriptor(
      name='packet', full_name='lum.network.icacallbacks.IcacallbacksPacketData.packet',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=67,
  serialized_end=154,
)


_NODATA = _descriptor.Descriptor(
  name='NoData',
  full_name='lum.network.icacallbacks.NoData',
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
  serialized_start=156,
  serialized_end=164,
)

_ICACALLBACKSPACKETDATA.fields_by_name['no_data'].message_type = _NODATA
_ICACALLBACKSPACKETDATA.oneofs_by_name['packet'].fields.append(
  _ICACALLBACKSPACKETDATA.fields_by_name['no_data'])
_ICACALLBACKSPACKETDATA.fields_by_name['no_data'].containing_oneof = _ICACALLBACKSPACKETDATA.oneofs_by_name['packet']
DESCRIPTOR.message_types_by_name['IcacallbacksPacketData'] = _ICACALLBACKSPACKETDATA
DESCRIPTOR.message_types_by_name['NoData'] = _NODATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IcacallbacksPacketData = _reflection.GeneratedProtocolMessageType('IcacallbacksPacketData', (_message.Message,), dict(
  DESCRIPTOR = _ICACALLBACKSPACKETDATA,
  __module__ = 'lum_network.icacallbacks.packet_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.icacallbacks.IcacallbacksPacketData)
  ))
_sym_db.RegisterMessage(IcacallbacksPacketData)

NoData = _reflection.GeneratedProtocolMessageType('NoData', (_message.Message,), dict(
  DESCRIPTOR = _NODATA,
  __module__ = 'lum_network.icacallbacks.packet_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.icacallbacks.NoData)
  ))
_sym_db.RegisterMessage(NoData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z1github.com/lum-network/chain/x/icacallbacks/types'))
# @@protoc_insertion_point(module_scope)
