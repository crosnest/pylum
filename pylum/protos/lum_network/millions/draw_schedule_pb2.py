# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/millions/draw_schedule.proto

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
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lum-network/millions/draw_schedule.proto',
  package='lum.network.millions',
  syntax='proto3',
  serialized_pb=_b('\n(lum-network/millions/draw_schedule.proto\x12\x14lum.network.millions\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x86\x01\n\x0c\x44rawSchedule\x12=\n\x0finitial_draw_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x37\n\ndraw_delta\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\x98\xdf\x1f\x01\xc8\xde\x1f\x00\x42/Z-github.com/lum-network/chain/x/millions/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_DRAWSCHEDULE = _descriptor.Descriptor(
  name='DrawSchedule',
  full_name='lum.network.millions.DrawSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initial_draw_at', full_name='lum.network.millions.DrawSchedule.initial_draw_at', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='draw_delta', full_name='lum.network.millions.DrawSchedule.draw_delta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=154,
  serialized_end=288,
)

_DRAWSCHEDULE.fields_by_name['initial_draw_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DRAWSCHEDULE.fields_by_name['draw_delta'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['DrawSchedule'] = _DRAWSCHEDULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DrawSchedule = _reflection.GeneratedProtocolMessageType('DrawSchedule', (_message.Message,), dict(
  DESCRIPTOR = _DRAWSCHEDULE,
  __module__ = 'lum_network.millions.draw_schedule_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.millions.DrawSchedule)
  ))
_sym_db.RegisterMessage(DrawSchedule)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z-github.com/lum-network/chain/x/millions/types'))
_DRAWSCHEDULE.fields_by_name['initial_draw_at'].has_options = True
_DRAWSCHEDULE.fields_by_name['initial_draw_at']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000'))
_DRAWSCHEDULE.fields_by_name['draw_delta'].has_options = True
_DRAWSCHEDULE.fields_by_name['draw_delta']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\000'))
# @@protoc_insertion_point(module_scope)