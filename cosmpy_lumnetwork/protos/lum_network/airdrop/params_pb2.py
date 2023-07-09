# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/airdrop/params.proto

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
  name='lum-network/airdrop/params.proto',
  package='lum.network.airdrop',
  syntax='proto3',
  serialized_pb=_b('\n lum-network/airdrop/params.proto\x12\x13lum.network.airdrop\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfc\x02\n\x06Params\x12]\n\x12\x61irdrop_start_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB%\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:\"airdrop_start_time\"\x12\x82\x01\n\x14\x64uration_until_decay\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationBI\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xea\xde\x1f\x1e\x64uration_until_decay,omitempty\xf2\xde\x1f\x1byaml:\"duration_until_decay\"\x12y\n\x11\x64uration_of_decay\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationBC\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xea\xde\x1f\x1b\x64uration_of_decay,omitempty\xf2\xde\x1f\x18yaml:\"duration_of_decay\"\x12\x13\n\x0b\x63laim_denom\x18\x04 \x01(\tB.Z,github.com/lum-network/chain/x/airdrop/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='lum.network.airdrop.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='airdrop_start_time', full_name='lum.network.airdrop.Params.airdrop_start_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000\362\336\037\031yaml:\"airdrop_start_time\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_until_decay', full_name='lum.network.airdrop.Params.duration_until_decay', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001\352\336\037\036duration_until_decay,omitempty\362\336\037\033yaml:\"duration_until_decay\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_of_decay', full_name='lum.network.airdrop.Params.duration_of_decay', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001\352\336\037\033duration_of_decay,omitempty\362\336\037\030yaml:\"duration_of_decay\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claim_denom', full_name='lum.network.airdrop.Params.claim_denom', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=145,
  serialized_end=525,
)

_PARAMS.fields_by_name['airdrop_start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PARAMS.fields_by_name['duration_until_decay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PARAMS.fields_by_name['duration_of_decay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
  DESCRIPTOR = _PARAMS,
  __module__ = 'lum_network.airdrop.params_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.airdrop.Params)
  ))
_sym_db.RegisterMessage(Params)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z,github.com/lum-network/chain/x/airdrop/types'))
_PARAMS.fields_by_name['airdrop_start_time'].has_options = True
_PARAMS.fields_by_name['airdrop_start_time']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000\362\336\037\031yaml:\"airdrop_start_time\"'))
_PARAMS.fields_by_name['duration_until_decay'].has_options = True
_PARAMS.fields_by_name['duration_until_decay']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001\352\336\037\036duration_until_decay,omitempty\362\336\037\033yaml:\"duration_until_decay\"'))
_PARAMS.fields_by_name['duration_of_decay'].has_options = True
_PARAMS.fields_by_name['duration_of_decay']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001\352\336\037\033duration_of_decay,omitempty\362\336\037\030yaml:\"duration_of_decay\"'))
# @@protoc_insertion_point(module_scope)
