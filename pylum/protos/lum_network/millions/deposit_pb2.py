# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/millions/deposit.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lum-network/millions/deposit.proto',
  package='lum.network.millions',
  syntax='proto3',
  serialized_pb=_b('\n\"lum-network/millions/deposit.proto\x12\x14lum.network.millions\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xf6\x03\n\x07\x44\x65posit\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x12\n\ndeposit_id\x18\x02 \x01(\x04\x12\x31\n\x05state\x18\x03 \x01(\x0e\x32\".lum.network.millions.DepositState\x12\x37\n\x0b\x65rror_state\x18\x04 \x01(\x0e\x32\".lum.network.millions.DepositState\x12\x33\n\x11\x64\x65positor_address\x18\x05 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12/\n\x06\x61mount\x18\x06 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x30\n\x0ewinner_address\x18\x07 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x12\n\nis_sponsor\x18\x08 \x01(\x08\x12\x19\n\x11\x63reated_at_height\x18\n \x01(\x03\x12\x19\n\x11updated_at_height\x18\x0b \x01(\x03\x12\x38\n\ncreated_at\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x38\n\nupdated_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00J\x04\x08\t\x10\n*\xf6\x01\n\x0c\x44\x65positState\x12.\n\x19\x44\x45POSIT_STATE_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUnspecified\x12/\n\x1a\x44\x45POSIT_STATE_IBC_TRANSFER\x10\x01\x1a\x0f\x8a\x9d \x0bIbcTransfer\x12/\n\x1a\x44\x45POSIT_STATE_ICA_DELEGATE\x10\x02\x1a\x0f\x8a\x9d \x0bIcaDelegate\x12&\n\x15\x44\x45POSIT_STATE_SUCCESS\x10\x03\x1a\x0b\x8a\x9d \x07Success\x12&\n\x15\x44\x45POSIT_STATE_FAILURE\x10\x04\x1a\x0b\x8a\x9d \x07\x46\x61ilure\x1a\x04\x88\xa3\x1e\x01\x42/Z-github.com/lum-network/chain/x/millions/typesb\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])

_DEPOSITSTATE = _descriptor.EnumDescriptor(
  name='DepositState',
  full_name='lum.network.millions.DepositState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEPOSIT_STATE_UNSPECIFIED', index=0, number=0,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \013Unspecified')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPOSIT_STATE_IBC_TRANSFER', index=1, number=1,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \013IbcTransfer')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPOSIT_STATE_ICA_DELEGATE', index=2, number=2,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \013IcaDelegate')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPOSIT_STATE_SUCCESS', index=3, number=3,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \007Success')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPOSIT_STATE_FAILURE', index=4, number=4,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \007Failure')),
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\210\243\036\001')),
  serialized_start=680,
  serialized_end=926,
)
_sym_db.RegisterEnumDescriptor(_DEPOSITSTATE)

DepositState = enum_type_wrapper.EnumTypeWrapper(_DEPOSITSTATE)
DEPOSIT_STATE_UNSPECIFIED = 0
DEPOSIT_STATE_IBC_TRANSFER = 1
DEPOSIT_STATE_ICA_DELEGATE = 2
DEPOSIT_STATE_SUCCESS = 3
DEPOSIT_STATE_FAILURE = 4



_DEPOSIT = _descriptor.Descriptor(
  name='Deposit',
  full_name='lum.network.millions.Deposit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pool_id', full_name='lum.network.millions.Deposit.pool_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deposit_id', full_name='lum.network.millions.Deposit.deposit_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='lum.network.millions.Deposit.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_state', full_name='lum.network.millions.Deposit.error_state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depositor_address', full_name='lum.network.millions.Deposit.depositor_address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='lum.network.millions.Deposit.amount', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='winner_address', full_name='lum.network.millions.Deposit.winner_address', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_sponsor', full_name='lum.network.millions.Deposit.is_sponsor', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at_height', full_name='lum.network.millions.Deposit.created_at_height', index=8,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at_height', full_name='lum.network.millions.Deposit.updated_at_height', index=9,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='lum.network.millions.Deposit.created_at', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='lum.network.millions.Deposit.updated_at', index=11,
      number=13, type=11, cpp_type=10, label=1,
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
  serialized_start=175,
  serialized_end=677,
)

_DEPOSIT.fields_by_name['state'].enum_type = _DEPOSITSTATE
_DEPOSIT.fields_by_name['error_state'].enum_type = _DEPOSITSTATE
_DEPOSIT.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_DEPOSIT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEPOSIT.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Deposit'] = _DEPOSIT
DESCRIPTOR.enum_types_by_name['DepositState'] = _DEPOSITSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Deposit = _reflection.GeneratedProtocolMessageType('Deposit', (_message.Message,), dict(
  DESCRIPTOR = _DEPOSIT,
  __module__ = 'lum_network.millions.deposit_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.millions.Deposit)
  ))
_sym_db.RegisterMessage(Deposit)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z-github.com/lum-network/chain/x/millions/types'))
_DEPOSITSTATE.has_options = True
_DEPOSITSTATE._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\210\243\036\001'))
_DEPOSITSTATE.values_by_name["DEPOSIT_STATE_UNSPECIFIED"].has_options = True
_DEPOSITSTATE.values_by_name["DEPOSIT_STATE_UNSPECIFIED"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \013Unspecified'))
_DEPOSITSTATE.values_by_name["DEPOSIT_STATE_IBC_TRANSFER"].has_options = True
_DEPOSITSTATE.values_by_name["DEPOSIT_STATE_IBC_TRANSFER"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \013IbcTransfer'))
_DEPOSITSTATE.values_by_name["DEPOSIT_STATE_ICA_DELEGATE"].has_options = True
_DEPOSITSTATE.values_by_name["DEPOSIT_STATE_ICA_DELEGATE"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \013IcaDelegate'))
_DEPOSITSTATE.values_by_name["DEPOSIT_STATE_SUCCESS"].has_options = True
_DEPOSITSTATE.values_by_name["DEPOSIT_STATE_SUCCESS"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \007Success'))
_DEPOSITSTATE.values_by_name["DEPOSIT_STATE_FAILURE"].has_options = True
_DEPOSITSTATE.values_by_name["DEPOSIT_STATE_FAILURE"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \007Failure'))
_DEPOSIT.fields_by_name['depositor_address'].has_options = True
_DEPOSIT.fields_by_name['depositor_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_DEPOSIT.fields_by_name['amount'].has_options = True
_DEPOSIT.fields_by_name['amount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_DEPOSIT.fields_by_name['winner_address'].has_options = True
_DEPOSIT.fields_by_name['winner_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322\264-\024cosmos.AddressString'))
_DEPOSIT.fields_by_name['created_at'].has_options = True
_DEPOSIT.fields_by_name['created_at']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000'))
_DEPOSIT.fields_by_name['updated_at'].has_options = True
_DEPOSIT.fields_by_name['updated_at']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
