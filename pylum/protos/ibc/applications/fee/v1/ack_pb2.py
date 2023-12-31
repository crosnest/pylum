# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/fee/v1/ack.proto

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
  name='ibc/applications/fee/v1/ack.proto',
  package='ibc.applications.fee.v1',
  syntax='proto3',
  serialized_pb=_b('\n!ibc/applications/fee/v1/ack.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\"\xe3\x01\n\x1bIncentivizedAcknowledgement\x12;\n\x13\x61pp_acknowledgement\x18\x01 \x01(\x0c\x42\x1e\xf2\xde\x1f\x1ayaml:\"app_acknowledgement\"\x12\x43\n\x17\x66orward_relayer_address\x18\x02 \x01(\tB\"\xf2\xde\x1f\x1eyaml:\"forward_relayer_address\"\x12\x42\n\x16underlying_app_success\x18\x03 \x01(\x08\x42\"\xf2\xde\x1f\x1eyaml:\"underlying_app_successl\"B7Z5github.com/cosmos/ibc-go/v5/modules/apps/29-fee/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_INCENTIVIZEDACKNOWLEDGEMENT = _descriptor.Descriptor(
  name='IncentivizedAcknowledgement',
  full_name='ibc.applications.fee.v1.IncentivizedAcknowledgement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_acknowledgement', full_name='ibc.applications.fee.v1.IncentivizedAcknowledgement.app_acknowledgement', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\032yaml:\"app_acknowledgement\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forward_relayer_address', full_name='ibc.applications.fee.v1.IncentivizedAcknowledgement.forward_relayer_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\036yaml:\"forward_relayer_address\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='underlying_app_success', full_name='ibc.applications.fee.v1.IncentivizedAcknowledgement.underlying_app_success', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\036yaml:\"underlying_app_successl\"')), file=DESCRIPTOR),
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
  serialized_start=85,
  serialized_end=312,
)

DESCRIPTOR.message_types_by_name['IncentivizedAcknowledgement'] = _INCENTIVIZEDACKNOWLEDGEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IncentivizedAcknowledgement = _reflection.GeneratedProtocolMessageType('IncentivizedAcknowledgement', (_message.Message,), dict(
  DESCRIPTOR = _INCENTIVIZEDACKNOWLEDGEMENT,
  __module__ = 'ibc.applications.fee.v1.ack_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.IncentivizedAcknowledgement)
  ))
_sym_db.RegisterMessage(IncentivizedAcknowledgement)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z5github.com/cosmos/ibc-go/v5/modules/apps/29-fee/types'))
_INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['app_acknowledgement'].has_options = True
_INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['app_acknowledgement']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\032yaml:\"app_acknowledgement\"'))
_INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['forward_relayer_address'].has_options = True
_INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['forward_relayer_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\036yaml:\"forward_relayer_address\"'))
_INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['underlying_app_success'].has_options = True
_INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['underlying_app_success']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\036yaml:\"underlying_app_successl\"'))
# @@protoc_insertion_point(module_scope)
