# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/fee/v1/fee.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/applications/fee/v1/fee.proto',
  package='ibc.applications.fee.v1',
  syntax='proto3',
  serialized_pb=_b('\n!ibc/applications/fee/v1/fee.proto\x12\x17ibc.applications.fee.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a!ibc/core/channel/v1/channel.proto\"\xdf\x02\n\x03\x46\x65\x65\x12p\n\x08recv_fee\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBC\xf2\xde\x1f\x0fyaml:\"recv_fee\"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12n\n\x07\x61\x63k_fee\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBB\xf2\xde\x1f\x0eyaml:\"ack_fee\"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12v\n\x0btimeout_fee\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xf2\xde\x1f\x12yaml:\"timeout_fee\"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\x81\x01\n\tPacketFee\x12/\n\x03\x66\x65\x65\x18\x01 \x01(\x0b\x32\x1c.ibc.applications.fee.v1.FeeB\x04\xc8\xde\x1f\x00\x12\x31\n\x0erefund_address\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:\"refund_address\"\x12\x10\n\x08relayers\x18\x03 \x03(\t\"a\n\nPacketFees\x12S\n\x0bpacket_fees\x18\x01 \x03(\x0b\x32\".ibc.applications.fee.v1.PacketFeeB\x1a\xf2\xde\x1f\x12yaml:\"packet_fees\"\xc8\xde\x1f\x00\"\xb7\x01\n\x14IdentifiedPacketFees\x12J\n\tpacket_id\x18\x01 \x01(\x0b\x32\x1d.ibc.core.channel.v1.PacketIdB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"packet_id\"\x12S\n\x0bpacket_fees\x18\x02 \x03(\x0b\x32\".ibc.applications.fee.v1.PacketFeeB\x1a\xf2\xde\x1f\x12yaml:\"packet_fees\"\xc8\xde\x1f\x00\x42\x37Z5github.com/cosmos/ibc-go/v5/modules/apps/29-fee/typesb\x06proto3')
  ,
  dependencies=[cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2.DESCRIPTOR,])




_FEE = _descriptor.Descriptor(
  name='Fee',
  full_name='ibc.applications.fee.v1.Fee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recv_fee', full_name='ibc.applications.fee.v1.Fee.recv_fee', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\017yaml:\"recv_fee\"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ack_fee', full_name='ibc.applications.fee.v1.Fee.ack_fee', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\016yaml:\"ack_fee\"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_fee', full_name='ibc.applications.fee.v1.Fee.timeout_fee', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\022yaml:\"timeout_fee\"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins')), file=DESCRIPTOR),
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
  serialized_start=152,
  serialized_end=503,
)


_PACKETFEE = _descriptor.Descriptor(
  name='PacketFee',
  full_name='ibc.applications.fee.v1.PacketFee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fee', full_name='ibc.applications.fee.v1.PacketFee.fee', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refund_address', full_name='ibc.applications.fee.v1.PacketFee.refund_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\025yaml:\"refund_address\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relayers', full_name='ibc.applications.fee.v1.PacketFee.relayers', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=506,
  serialized_end=635,
)


_PACKETFEES = _descriptor.Descriptor(
  name='PacketFees',
  full_name='ibc.applications.fee.v1.PacketFees',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packet_fees', full_name='ibc.applications.fee.v1.PacketFees.packet_fees', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\022yaml:\"packet_fees\"\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=637,
  serialized_end=734,
)


_IDENTIFIEDPACKETFEES = _descriptor.Descriptor(
  name='IdentifiedPacketFees',
  full_name='ibc.applications.fee.v1.IdentifiedPacketFees',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packet_id', full_name='ibc.applications.fee.v1.IdentifiedPacketFees.packet_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\362\336\037\020yaml:\"packet_id\"')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packet_fees', full_name='ibc.applications.fee.v1.IdentifiedPacketFees.packet_fees', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\022yaml:\"packet_fees\"\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=737,
  serialized_end=920,
)

_FEE.fields_by_name['recv_fee'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_FEE.fields_by_name['ack_fee'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_FEE.fields_by_name['timeout_fee'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_PACKETFEE.fields_by_name['fee'].message_type = _FEE
_PACKETFEES.fields_by_name['packet_fees'].message_type = _PACKETFEE
_IDENTIFIEDPACKETFEES.fields_by_name['packet_id'].message_type = ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2._PACKETID
_IDENTIFIEDPACKETFEES.fields_by_name['packet_fees'].message_type = _PACKETFEE
DESCRIPTOR.message_types_by_name['Fee'] = _FEE
DESCRIPTOR.message_types_by_name['PacketFee'] = _PACKETFEE
DESCRIPTOR.message_types_by_name['PacketFees'] = _PACKETFEES
DESCRIPTOR.message_types_by_name['IdentifiedPacketFees'] = _IDENTIFIEDPACKETFEES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Fee = _reflection.GeneratedProtocolMessageType('Fee', (_message.Message,), dict(
  DESCRIPTOR = _FEE,
  __module__ = 'ibc.applications.fee.v1.fee_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.Fee)
  ))
_sym_db.RegisterMessage(Fee)

PacketFee = _reflection.GeneratedProtocolMessageType('PacketFee', (_message.Message,), dict(
  DESCRIPTOR = _PACKETFEE,
  __module__ = 'ibc.applications.fee.v1.fee_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.PacketFee)
  ))
_sym_db.RegisterMessage(PacketFee)

PacketFees = _reflection.GeneratedProtocolMessageType('PacketFees', (_message.Message,), dict(
  DESCRIPTOR = _PACKETFEES,
  __module__ = 'ibc.applications.fee.v1.fee_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.PacketFees)
  ))
_sym_db.RegisterMessage(PacketFees)

IdentifiedPacketFees = _reflection.GeneratedProtocolMessageType('IdentifiedPacketFees', (_message.Message,), dict(
  DESCRIPTOR = _IDENTIFIEDPACKETFEES,
  __module__ = 'ibc.applications.fee.v1.fee_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.IdentifiedPacketFees)
  ))
_sym_db.RegisterMessage(IdentifiedPacketFees)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z5github.com/cosmos/ibc-go/v5/modules/apps/29-fee/types'))
_FEE.fields_by_name['recv_fee'].has_options = True
_FEE.fields_by_name['recv_fee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\017yaml:\"recv_fee\"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'))
_FEE.fields_by_name['ack_fee'].has_options = True
_FEE.fields_by_name['ack_fee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\016yaml:\"ack_fee\"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'))
_FEE.fields_by_name['timeout_fee'].has_options = True
_FEE.fields_by_name['timeout_fee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\022yaml:\"timeout_fee\"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'))
_PACKETFEE.fields_by_name['fee'].has_options = True
_PACKETFEE.fields_by_name['fee']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_PACKETFEE.fields_by_name['refund_address'].has_options = True
_PACKETFEE.fields_by_name['refund_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\025yaml:\"refund_address\"'))
_PACKETFEES.fields_by_name['packet_fees'].has_options = True
_PACKETFEES.fields_by_name['packet_fees']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\022yaml:\"packet_fees\"\310\336\037\000'))
_IDENTIFIEDPACKETFEES.fields_by_name['packet_id'].has_options = True
_IDENTIFIEDPACKETFEES.fields_by_name['packet_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\362\336\037\020yaml:\"packet_id\"'))
_IDENTIFIEDPACKETFEES.fields_by_name['packet_fees'].has_options = True
_IDENTIFIEDPACKETFEES.fields_by_name['packet_fees']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\362\336\037\022yaml:\"packet_fees\"\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
