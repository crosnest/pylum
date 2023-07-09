# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/millions/pool.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from lum_network.millions import draw_pb2 as lum__network_dot_millions_dot_draw__pb2
from lum_network.millions import draw_schedule_pb2 as lum__network_dot_millions_dot_draw__schedule__pb2
from lum_network.millions import prize_strategy_pb2 as lum__network_dot_millions_dot_prize__strategy__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lum-network/millions/pool.proto',
  package='lum.network.millions',
  syntax='proto3',
  serialized_pb=_b('\n\x1flum-network/millions/pool.proto\x12\x14lum.network.millions\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1flum-network/millions/draw.proto\x1a(lum-network/millions/draw_schedule.proto\x1a)lum-network/millions/prize_strategy.proto\"\xaf\n\n\x04Pool\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\x12\x14\n\x0cnative_denom\x18\x03 \x01(\t\x12\x10\n\x08\x63hain_id\x18\x04 \x01(\t\x12\x15\n\rconnection_id\x18\x05 \x01(\t\x12\x1b\n\x13transfer_channel_id\x18\x06 \x01(\t\x12\x1b\n\x13ica_deposit_port_id\x18\x07 \x01(\t\x12\x1d\n\x15ica_prizepool_port_id\x18\x08 \x01(\t\x12=\n\nvalidators\x18\n \x03(\x0b\x32#.lum.network.millions.PoolValidatorB\x04\xc8\xde\x1f\x00\x12\x1e\n\x16\x62\x65\x63h32_prefix_acc_addr\x18\x0b \x01(\t\x12\x1e\n\x16\x62\x65\x63h32_prefix_val_addr\x18\x0c \x01(\t\x12J\n\x12min_deposit_amount\x18\r \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12?\n\rdraw_schedule\x18\x0e \x01(\x0b\x32\".lum.network.millions.DrawScheduleB\x04\xc8\xde\x1f\x00\x12\x41\n\x0eprize_strategy\x18\x0f \x01(\x0b\x32#.lum.network.millions.PrizeStrategyB\x04\xc8\xde\x1f\x00\x12/\n\rlocal_address\x18\x12 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x35\n\x13ica_deposit_address\x18\x13 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x37\n\x15ica_prizepool_address\x18\x14 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x14\n\x0cnext_draw_id\x18\x16 \x01(\x04\x12\x42\n\ntvl_amount\x18\x17 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x18\n\x10\x64\x65positors_count\x18\x18 \x01(\x04\x12J\n\x12sponsorship_amount\x18\x19 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x42\n\x14last_draw_created_at\x18\x1b \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x01\x12\x38\n\x0flast_draw_state\x18\x1c \x01(\x0e\x32\x1f.lum.network.millions.DrawState\x12=\n\x14\x61vailable_prize_pool\x18\x1d \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12.\n\x05state\x18  \x01(\x0e\x32\x1f.lum.network.millions.PoolState\x12\x19\n\x11\x63reated_at_height\x18! \x01(\x03\x12\x19\n\x11updated_at_height\x18\" \x01(\x03\x12\x38\n\ncreated_at\x18# \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x38\n\nupdated_at\x18$ \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00J\x04\x08\t\x10\nJ\x04\x08\x10\x10\x11J\x04\x08\x11\x10\x12J\x04\x08\x15\x10\x16J\x04\x08\x1a\x10\x1bJ\x04\x08\x1e\x10\x1fJ\x04\x08\x1f\x10 \"\x9e\x01\n\rPoolValidator\x12\x32\n\x10operator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x12\n\nis_enabled\x18\x02 \x01(\x08\x12\x45\n\rbonded_amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00*\xca\x01\n\tPoolState\x12+\n\x16POOL_STATE_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUnspecified\x12#\n\x12POOL_STATE_CREATED\x10\x01\x1a\x0b\x8a\x9d \x07\x43reated\x12\x1f\n\x10POOL_STATE_READY\x10\x02\x1a\t\x8a\x9d \x05Ready\x12!\n\x11POOL_STATE_PAUSED\x10\x03\x1a\n\x8a\x9d \x06Paused\x12!\n\x11POOL_STATE_KILLED\x10\x04\x1a\n\x8a\x9d \x06Killed\x1a\x04\x88\xa3\x1e\x01\x42/Z-github.com/lum-network/chain/x/millions/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,lum__network_dot_millions_dot_draw__pb2.DESCRIPTOR,lum__network_dot_millions_dot_draw__schedule__pb2.DESCRIPTOR,lum__network_dot_millions_dot_prize__strategy__pb2.DESCRIPTOR,])

_POOLSTATE = _descriptor.EnumDescriptor(
  name='PoolState',
  full_name='lum.network.millions.PoolState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POOL_STATE_UNSPECIFIED', index=0, number=0,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \013Unspecified')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POOL_STATE_CREATED', index=1, number=1,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \007Created')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POOL_STATE_READY', index=2, number=2,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \005Ready')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POOL_STATE_PAUSED', index=3, number=3,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \006Paused')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POOL_STATE_KILLED', index=4, number=4,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \006Killed')),
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\210\243\036\001')),
  serialized_start=1781,
  serialized_end=1983,
)
_sym_db.RegisterEnumDescriptor(_POOLSTATE)

PoolState = enum_type_wrapper.EnumTypeWrapper(_POOLSTATE)
POOL_STATE_UNSPECIFIED = 0
POOL_STATE_CREATED = 1
POOL_STATE_READY = 2
POOL_STATE_PAUSED = 3
POOL_STATE_KILLED = 4



_POOL = _descriptor.Descriptor(
  name='Pool',
  full_name='lum.network.millions.Pool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pool_id', full_name='lum.network.millions.Pool.pool_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denom', full_name='lum.network.millions.Pool.denom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='native_denom', full_name='lum.network.millions.Pool.native_denom', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='lum.network.millions.Pool.chain_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='lum.network.millions.Pool.connection_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer_channel_id', full_name='lum.network.millions.Pool.transfer_channel_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ica_deposit_port_id', full_name='lum.network.millions.Pool.ica_deposit_port_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ica_prizepool_port_id', full_name='lum.network.millions.Pool.ica_prizepool_port_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validators', full_name='lum.network.millions.Pool.validators', index=8,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bech32_prefix_acc_addr', full_name='lum.network.millions.Pool.bech32_prefix_acc_addr', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bech32_prefix_val_addr', full_name='lum.network.millions.Pool.bech32_prefix_val_addr', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_deposit_amount', full_name='lum.network.millions.Pool.min_deposit_amount', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='draw_schedule', full_name='lum.network.millions.Pool.draw_schedule', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prize_strategy', full_name='lum.network.millions.Pool.prize_strategy', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_address', full_name='lum.network.millions.Pool.local_address', index=14,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ica_deposit_address', full_name='lum.network.millions.Pool.ica_deposit_address', index=15,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ica_prizepool_address', full_name='lum.network.millions.Pool.ica_prizepool_address', index=16,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_draw_id', full_name='lum.network.millions.Pool.next_draw_id', index=17,
      number=22, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tvl_amount', full_name='lum.network.millions.Pool.tvl_amount', index=18,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depositors_count', full_name='lum.network.millions.Pool.depositors_count', index=19,
      number=24, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sponsorship_amount', full_name='lum.network.millions.Pool.sponsorship_amount', index=20,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_draw_created_at', full_name='lum.network.millions.Pool.last_draw_created_at', index=21,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_draw_state', full_name='lum.network.millions.Pool.last_draw_state', index=22,
      number=28, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_prize_pool', full_name='lum.network.millions.Pool.available_prize_pool', index=23,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='lum.network.millions.Pool.state', index=24,
      number=32, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at_height', full_name='lum.network.millions.Pool.created_at_height', index=25,
      number=33, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at_height', full_name='lum.network.millions.Pool.updated_at_height', index=26,
      number=34, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='lum.network.millions.Pool.created_at', index=27,
      number=35, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='lum.network.millions.Pool.updated_at', index=28,
      number=36, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=290,
  serialized_end=1617,
)


_POOLVALIDATOR = _descriptor.Descriptor(
  name='PoolValidator',
  full_name='lum.network.millions.PoolValidator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operator_address', full_name='lum.network.millions.PoolValidator.operator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_enabled', full_name='lum.network.millions.PoolValidator.is_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bonded_amount', full_name='lum.network.millions.PoolValidator.bonded_amount', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=1620,
  serialized_end=1778,
)

_POOL.fields_by_name['validators'].message_type = _POOLVALIDATOR
_POOL.fields_by_name['draw_schedule'].message_type = lum__network_dot_millions_dot_draw__schedule__pb2._DRAWSCHEDULE
_POOL.fields_by_name['prize_strategy'].message_type = lum__network_dot_millions_dot_prize__strategy__pb2._PRIZESTRATEGY
_POOL.fields_by_name['last_draw_created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_POOL.fields_by_name['last_draw_state'].enum_type = lum__network_dot_millions_dot_draw__pb2._DRAWSTATE
_POOL.fields_by_name['available_prize_pool'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_POOL.fields_by_name['state'].enum_type = _POOLSTATE
_POOL.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_POOL.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Pool'] = _POOL
DESCRIPTOR.message_types_by_name['PoolValidator'] = _POOLVALIDATOR
DESCRIPTOR.enum_types_by_name['PoolState'] = _POOLSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pool = _reflection.GeneratedProtocolMessageType('Pool', (_message.Message,), dict(
  DESCRIPTOR = _POOL,
  __module__ = 'lum_network.millions.pool_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.millions.Pool)
  ))
_sym_db.RegisterMessage(Pool)

PoolValidator = _reflection.GeneratedProtocolMessageType('PoolValidator', (_message.Message,), dict(
  DESCRIPTOR = _POOLVALIDATOR,
  __module__ = 'lum_network.millions.pool_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.millions.PoolValidator)
  ))
_sym_db.RegisterMessage(PoolValidator)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z-github.com/lum-network/chain/x/millions/types'))
_POOLSTATE.has_options = True
_POOLSTATE._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\210\243\036\001'))
_POOLSTATE.values_by_name["POOL_STATE_UNSPECIFIED"].has_options = True
_POOLSTATE.values_by_name["POOL_STATE_UNSPECIFIED"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \013Unspecified'))
_POOLSTATE.values_by_name["POOL_STATE_CREATED"].has_options = True
_POOLSTATE.values_by_name["POOL_STATE_CREATED"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \007Created'))
_POOLSTATE.values_by_name["POOL_STATE_READY"].has_options = True
_POOLSTATE.values_by_name["POOL_STATE_READY"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \005Ready'))
_POOLSTATE.values_by_name["POOL_STATE_PAUSED"].has_options = True
_POOLSTATE.values_by_name["POOL_STATE_PAUSED"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \006Paused'))
_POOLSTATE.values_by_name["POOL_STATE_KILLED"].has_options = True
_POOLSTATE.values_by_name["POOL_STATE_KILLED"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \006Killed'))
_POOL.fields_by_name['validators'].has_options = True
_POOL.fields_by_name['validators']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_POOL.fields_by_name['min_deposit_amount'].has_options = True
_POOL.fields_by_name['min_deposit_amount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'))
_POOL.fields_by_name['draw_schedule'].has_options = True
_POOL.fields_by_name['draw_schedule']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_POOL.fields_by_name['prize_strategy'].has_options = True
_POOL.fields_by_name['prize_strategy']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_POOL.fields_by_name['local_address'].has_options = True
_POOL.fields_by_name['local_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_POOL.fields_by_name['ica_deposit_address'].has_options = True
_POOL.fields_by_name['ica_deposit_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_POOL.fields_by_name['ica_prizepool_address'].has_options = True
_POOL.fields_by_name['ica_prizepool_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_POOL.fields_by_name['tvl_amount'].has_options = True
_POOL.fields_by_name['tvl_amount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'))
_POOL.fields_by_name['sponsorship_amount'].has_options = True
_POOL.fields_by_name['sponsorship_amount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'))
_POOL.fields_by_name['last_draw_created_at'].has_options = True
_POOL.fields_by_name['last_draw_created_at']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\001'))
_POOL.fields_by_name['available_prize_pool'].has_options = True
_POOL.fields_by_name['available_prize_pool']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_POOL.fields_by_name['created_at'].has_options = True
_POOL.fields_by_name['created_at']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000'))
_POOL.fields_by_name['updated_at'].has_options = True
_POOL.fields_by_name['updated_at']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000'))
_POOLVALIDATOR.fields_by_name['operator_address'].has_options = True
_POOLVALIDATOR.fields_by_name['operator_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_POOLVALIDATOR.fields_by_name['bonded_amount'].has_options = True
_POOLVALIDATOR.fields_by_name['bonded_amount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'))
# @@protoc_insertion_point(module_scope)