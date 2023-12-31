# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/millions/gov.proto

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
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from lum_network.millions import draw_schedule_pb2 as lum__network_dot_millions_dot_draw__schedule__pb2
from lum_network.millions import prize_strategy_pb2 as lum__network_dot_millions_dot_prize__strategy__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lum-network/millions/gov.proto',
  package='lum.network.millions',
  syntax='proto3',
  serialized_pb=_b('\n\x1elum-network/millions/gov.proto\x12\x14lum.network.millions\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a(lum-network/millions/draw_schedule.proto\x1a)lum-network/millions/prize_strategy.proto\"\xcf\x03\n\x14ProposalRegisterPool\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08\x63hain_id\x18\x03 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x04 \x01(\t\x12\x14\n\x0cnative_denom\x18\x05 \x01(\t\x12\x15\n\rconnection_id\x18\x06 \x01(\t\x12\x12\n\nvalidators\x18\x07 \x03(\t\x12J\n\x12min_deposit_amount\x18\x08 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12?\n\rdraw_schedule\x18\t \x01(\x0b\x32\".lum.network.millions.DrawScheduleB\x04\xc8\xde\x1f\x00\x12\x41\n\x0eprize_strategy\x18\n \x01(\x0b\x32#.lum.network.millions.PrizeStrategyB\x04\xc8\xde\x1f\x00\x12\x1e\n\x16\x62\x65\x63h32_prefix_acc_addr\x18\x0b \x01(\t\x12\x1e\n\x16\x62\x65\x63h32_prefix_val_addr\x18\x0c \x01(\t\x12\x1b\n\x13transfer_channel_id\x18\r \x01(\t:\x04\x98\xa0\x1f\x00\"\xb9\x02\n\x12ProposalUpdatePool\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07pool_id\x18\x03 \x01(\x04\x12\x18\n\nvalidators\x18\x04 \x03(\tB\x04\xc8\xde\x1f\x01\x12J\n\x12min_deposit_amount\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x01\x12?\n\rdraw_schedule\x18\x06 \x01(\x0b\x32\".lum.network.millions.DrawScheduleB\x04\xc8\xde\x1f\x01\x12\x41\n\x0eprize_strategy\x18\x07 \x01(\x0b\x32#.lum.network.millions.PrizeStrategyB\x04\xc8\xde\x1f\x01:\x04\x98\xa0\x1f\x00\"\x8e\x05\n\x14ProposalUpdateParams\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12J\n\x12min_deposit_amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x01\x12R\n\x1amax_prize_strategy_batches\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x01\x12P\n\x18max_prize_batch_quantity\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x01\x12\x44\n\x17min_draw_schedule_delta\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\x98\xdf\x1f\x01\xc8\xde\x1f\x01\x12\x44\n\x17max_draw_schedule_delta\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\x98\xdf\x1f\x01\xc8\xde\x1f\x01\x12\x43\n\x16prize_expiration_delta\x18\x08 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\x98\xdf\x1f\x01\xc8\xde\x1f\x01\x12\x44\n\x0c\x66\x65\x65s_stakers\x18\t \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x01\x12\x43\n\x16min_deposit_draw_delta\x18\n \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\x98\xdf\x1f\x01\xc8\xde\x1f\x01:\x04\x98\xa0\x1f\x00\x42/Z-github.com/lum-network/chain/x/millions/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,lum__network_dot_millions_dot_draw__schedule__pb2.DESCRIPTOR,lum__network_dot_millions_dot_prize__strategy__pb2.DESCRIPTOR,])




_PROPOSALREGISTERPOOL = _descriptor.Descriptor(
  name='ProposalRegisterPool',
  full_name='lum.network.millions.ProposalRegisterPool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='lum.network.millions.ProposalRegisterPool.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='lum.network.millions.ProposalRegisterPool.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='lum.network.millions.ProposalRegisterPool.chain_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denom', full_name='lum.network.millions.ProposalRegisterPool.denom', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='native_denom', full_name='lum.network.millions.ProposalRegisterPool.native_denom', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='lum.network.millions.ProposalRegisterPool.connection_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validators', full_name='lum.network.millions.ProposalRegisterPool.validators', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_deposit_amount', full_name='lum.network.millions.ProposalRegisterPool.min_deposit_amount', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='draw_schedule', full_name='lum.network.millions.ProposalRegisterPool.draw_schedule', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prize_strategy', full_name='lum.network.millions.ProposalRegisterPool.prize_strategy', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bech32_prefix_acc_addr', full_name='lum.network.millions.ProposalRegisterPool.bech32_prefix_acc_addr', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bech32_prefix_val_addr', full_name='lum.network.millions.ProposalRegisterPool.bech32_prefix_val_addr', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer_channel_id', full_name='lum.network.millions.ProposalRegisterPool.transfer_channel_id', index=12,
      number=13, type=9, cpp_type=9, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=718,
)


_PROPOSALUPDATEPOOL = _descriptor.Descriptor(
  name='ProposalUpdatePool',
  full_name='lum.network.millions.ProposalUpdatePool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='lum.network.millions.ProposalUpdatePool.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='lum.network.millions.ProposalUpdatePool.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pool_id', full_name='lum.network.millions.ProposalUpdatePool.pool_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validators', full_name='lum.network.millions.ProposalUpdatePool.validators', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_deposit_amount', full_name='lum.network.millions.ProposalUpdatePool.min_deposit_amount', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='draw_schedule', full_name='lum.network.millions.ProposalUpdatePool.draw_schedule', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prize_strategy', full_name='lum.network.millions.ProposalUpdatePool.prize_strategy', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\001')), file=DESCRIPTOR),
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
  serialized_start=721,
  serialized_end=1034,
)


_PROPOSALUPDATEPARAMS = _descriptor.Descriptor(
  name='ProposalUpdateParams',
  full_name='lum.network.millions.ProposalUpdateParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='lum.network.millions.ProposalUpdateParams.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='lum.network.millions.ProposalUpdateParams.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_deposit_amount', full_name='lum.network.millions.ProposalUpdateParams.min_deposit_amount', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_prize_strategy_batches', full_name='lum.network.millions.ProposalUpdateParams.max_prize_strategy_batches', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_prize_batch_quantity', full_name='lum.network.millions.ProposalUpdateParams.max_prize_batch_quantity', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_draw_schedule_delta', full_name='lum.network.millions.ProposalUpdateParams.min_draw_schedule_delta', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_draw_schedule_delta', full_name='lum.network.millions.ProposalUpdateParams.max_draw_schedule_delta', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prize_expiration_delta', full_name='lum.network.millions.ProposalUpdateParams.prize_expiration_delta', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fees_stakers', full_name='lum.network.millions.ProposalUpdateParams.fees_stakers', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_deposit_draw_delta', full_name='lum.network.millions.ProposalUpdateParams.min_deposit_draw_delta', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\001')), file=DESCRIPTOR),
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
  serialized_start=1037,
  serialized_end=1691,
)

_PROPOSALREGISTERPOOL.fields_by_name['draw_schedule'].message_type = lum__network_dot_millions_dot_draw__schedule__pb2._DRAWSCHEDULE
_PROPOSALREGISTERPOOL.fields_by_name['prize_strategy'].message_type = lum__network_dot_millions_dot_prize__strategy__pb2._PRIZESTRATEGY
_PROPOSALUPDATEPOOL.fields_by_name['draw_schedule'].message_type = lum__network_dot_millions_dot_draw__schedule__pb2._DRAWSCHEDULE
_PROPOSALUPDATEPOOL.fields_by_name['prize_strategy'].message_type = lum__network_dot_millions_dot_prize__strategy__pb2._PRIZESTRATEGY
_PROPOSALUPDATEPARAMS.fields_by_name['min_draw_schedule_delta'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PROPOSALUPDATEPARAMS.fields_by_name['max_draw_schedule_delta'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PROPOSALUPDATEPARAMS.fields_by_name['prize_expiration_delta'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PROPOSALUPDATEPARAMS.fields_by_name['min_deposit_draw_delta'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['ProposalRegisterPool'] = _PROPOSALREGISTERPOOL
DESCRIPTOR.message_types_by_name['ProposalUpdatePool'] = _PROPOSALUPDATEPOOL
DESCRIPTOR.message_types_by_name['ProposalUpdateParams'] = _PROPOSALUPDATEPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProposalRegisterPool = _reflection.GeneratedProtocolMessageType('ProposalRegisterPool', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSALREGISTERPOOL,
  __module__ = 'lum_network.millions.gov_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.millions.ProposalRegisterPool)
  ))
_sym_db.RegisterMessage(ProposalRegisterPool)

ProposalUpdatePool = _reflection.GeneratedProtocolMessageType('ProposalUpdatePool', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSALUPDATEPOOL,
  __module__ = 'lum_network.millions.gov_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.millions.ProposalUpdatePool)
  ))
_sym_db.RegisterMessage(ProposalUpdatePool)

ProposalUpdateParams = _reflection.GeneratedProtocolMessageType('ProposalUpdateParams', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSALUPDATEPARAMS,
  __module__ = 'lum_network.millions.gov_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.millions.ProposalUpdateParams)
  ))
_sym_db.RegisterMessage(ProposalUpdateParams)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z-github.com/lum-network/chain/x/millions/types'))
_PROPOSALREGISTERPOOL.fields_by_name['min_deposit_amount'].has_options = True
_PROPOSALREGISTERPOOL.fields_by_name['min_deposit_amount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'))
_PROPOSALREGISTERPOOL.fields_by_name['draw_schedule'].has_options = True
_PROPOSALREGISTERPOOL.fields_by_name['draw_schedule']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_PROPOSALREGISTERPOOL.fields_by_name['prize_strategy'].has_options = True
_PROPOSALREGISTERPOOL.fields_by_name['prize_strategy']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_PROPOSALREGISTERPOOL.has_options = True
_PROPOSALREGISTERPOOL._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000'))
_PROPOSALUPDATEPOOL.fields_by_name['validators'].has_options = True
_PROPOSALUPDATEPOOL.fields_by_name['validators']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\001'))
_PROPOSALUPDATEPOOL.fields_by_name['min_deposit_amount'].has_options = True
_PROPOSALUPDATEPOOL.fields_by_name['min_deposit_amount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\001'))
_PROPOSALUPDATEPOOL.fields_by_name['draw_schedule'].has_options = True
_PROPOSALUPDATEPOOL.fields_by_name['draw_schedule']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\001'))
_PROPOSALUPDATEPOOL.fields_by_name['prize_strategy'].has_options = True
_PROPOSALUPDATEPOOL.fields_by_name['prize_strategy']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\001'))
_PROPOSALUPDATEPOOL.has_options = True
_PROPOSALUPDATEPOOL._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000'))
_PROPOSALUPDATEPARAMS.fields_by_name['min_deposit_amount'].has_options = True
_PROPOSALUPDATEPARAMS.fields_by_name['min_deposit_amount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\001'))
_PROPOSALUPDATEPARAMS.fields_by_name['max_prize_strategy_batches'].has_options = True
_PROPOSALUPDATEPARAMS.fields_by_name['max_prize_strategy_batches']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\001'))
_PROPOSALUPDATEPARAMS.fields_by_name['max_prize_batch_quantity'].has_options = True
_PROPOSALUPDATEPARAMS.fields_by_name['max_prize_batch_quantity']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\001'))
_PROPOSALUPDATEPARAMS.fields_by_name['min_draw_schedule_delta'].has_options = True
_PROPOSALUPDATEPARAMS.fields_by_name['min_draw_schedule_delta']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\001'))
_PROPOSALUPDATEPARAMS.fields_by_name['max_draw_schedule_delta'].has_options = True
_PROPOSALUPDATEPARAMS.fields_by_name['max_draw_schedule_delta']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\001'))
_PROPOSALUPDATEPARAMS.fields_by_name['prize_expiration_delta'].has_options = True
_PROPOSALUPDATEPARAMS.fields_by_name['prize_expiration_delta']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\001'))
_PROPOSALUPDATEPARAMS.fields_by_name['fees_stakers'].has_options = True
_PROPOSALUPDATEPARAMS.fields_by_name['fees_stakers']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\001'))
_PROPOSALUPDATEPARAMS.fields_by_name['min_deposit_draw_delta'].has_options = True
_PROPOSALUPDATEPARAMS.fields_by_name['min_deposit_draw_delta']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\230\337\037\001\310\336\037\001'))
_PROPOSALUPDATEPARAMS.has_options = True
_PROPOSALUPDATEPARAMS._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\230\240\037\000'))
# @@protoc_insertion_point(module_scope)
