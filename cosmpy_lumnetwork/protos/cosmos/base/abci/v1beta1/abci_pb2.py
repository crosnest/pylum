# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/abci/v1beta1/abci.proto

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
from tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/base/abci/v1beta1/abci.proto',
  package='cosmos.base.abci.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n#cosmos/base/abci/v1beta1/abci.proto\x12\x18\x63osmos.base.abci.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1btendermint/abci/types.proto\x1a\x19google/protobuf/any.proto\"\xe6\x02\n\nTxResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x1a\n\x06txhash\x18\x02 \x01(\tB\n\xe2\xde\x1f\x06TxHash\x12\x11\n\tcodespace\x18\x03 \x01(\t\x12\x0c\n\x04\x63ode\x18\x04 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\t\x12\x0f\n\x07raw_log\x18\x06 \x01(\t\x12O\n\x04logs\x18\x07 \x03(\x0b\x32(.cosmos.base.abci.v1beta1.ABCIMessageLogB\x17\xaa\xdf\x1f\x0f\x41\x42\x43IMessageLogs\xc8\xde\x1f\x00\x12\x0c\n\x04info\x18\x08 \x01(\t\x12\x12\n\ngas_wanted\x18\t \x01(\x03\x12\x10\n\x08gas_used\x18\n \x01(\x03\x12 \n\x02tx\x18\x0b \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\ttimestamp\x18\x0c \x01(\t\x12,\n\x06\x65vents\x18\r \x03(\x0b\x32\x16.tendermint.abci.EventB\x04\xc8\xde\x1f\x00:\x04\x88\xa0\x1f\x00\"\x92\x01\n\x0e\x41\x42\x43IMessageLog\x12 \n\tmsg_index\x18\x01 \x01(\rB\r\xea\xde\x1f\tmsg_index\x12\x0b\n\x03log\x18\x02 \x01(\t\x12K\n\x06\x65vents\x18\x03 \x03(\x0b\x32%.cosmos.base.abci.v1beta1.StringEventB\x14\xaa\xdf\x1f\x0cStringEvents\xc8\xde\x1f\x00:\x04\x80\xdc \x01\"`\n\x0bStringEvent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12=\n\nattributes\x18\x02 \x03(\x0b\x32#.cosmos.base.abci.v1beta1.AttributeB\x04\xc8\xde\x1f\x00:\x04\x80\xdc \x01\"\'\n\tAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"/\n\x07GasInfo\x12\x12\n\ngas_wanted\x18\x01 \x01(\x04\x12\x10\n\x08gas_used\x18\x02 \x01(\x04\"\x88\x01\n\x06Result\x12\x10\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x42\x02\x18\x01\x12\x0b\n\x03log\x18\x02 \x01(\t\x12,\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x16.tendermint.abci.EventB\x04\xc8\xde\x1f\x00\x12+\n\rmsg_responses\x18\x04 \x03(\x0b\x32\x14.google.protobuf.Any:\x04\x88\xa0\x1f\x00\"\x85\x01\n\x12SimulationResponse\x12=\n\x08gas_info\x18\x01 \x01(\x0b\x32!.cosmos.base.abci.v1beta1.GasInfoB\x08\xd0\xde\x1f\x01\xc8\xde\x1f\x00\x12\x30\n\x06result\x18\x02 \x01(\x0b\x32 .cosmos.base.abci.v1beta1.Result\"1\n\x07MsgData\x12\x10\n\x08msg_type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c:\x06\x18\x01\x80\xdc \x01\"s\n\tTxMsgData\x12\x33\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32!.cosmos.base.abci.v1beta1.MsgDataB\x02\x18\x01\x12+\n\rmsg_responses\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any:\x04\x80\xdc \x01\"\xa6\x01\n\x0fSearchTxsResult\x12\x13\n\x0btotal_count\x18\x01 \x01(\x04\x12\r\n\x05\x63ount\x18\x02 \x01(\x04\x12\x13\n\x0bpage_number\x18\x03 \x01(\x04\x12\x12\n\npage_total\x18\x04 \x01(\x04\x12\r\n\x05limit\x18\x05 \x01(\x04\x12\x31\n\x03txs\x18\x06 \x03(\x0b\x32$.cosmos.base.abci.v1beta1.TxResponse:\x04\x80\xdc \x01\x42(Z\"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00\x62\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,tendermint_dot_abci_dot_types__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_TXRESPONSE = _descriptor.Descriptor(
  name='TxResponse',
  full_name='cosmos.base.abci.v1beta1.TxResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='cosmos.base.abci.v1beta1.TxResponse.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txhash', full_name='cosmos.base.abci.v1beta1.TxResponse.txhash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\006TxHash')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codespace', full_name='cosmos.base.abci.v1beta1.TxResponse.codespace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='cosmos.base.abci.v1beta1.TxResponse.code', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cosmos.base.abci.v1beta1.TxResponse.data', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_log', full_name='cosmos.base.abci.v1beta1.TxResponse.raw_log', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs', full_name='cosmos.base.abci.v1beta1.TxResponse.logs', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\017ABCIMessageLogs\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='cosmos.base.abci.v1beta1.TxResponse.info', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_wanted', full_name='cosmos.base.abci.v1beta1.TxResponse.gas_wanted', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_used', full_name='cosmos.base.abci.v1beta1.TxResponse.gas_used', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx', full_name='cosmos.base.abci.v1beta1.TxResponse.tx', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cosmos.base.abci.v1beta1.TxResponse.timestamp', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='cosmos.base.abci.v1beta1.TxResponse.events', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=502,
)


_ABCIMESSAGELOG = _descriptor.Descriptor(
  name='ABCIMessageLog',
  full_name='cosmos.base.abci.v1beta1.ABCIMessageLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_index', full_name='cosmos.base.abci.v1beta1.ABCIMessageLog.msg_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\tmsg_index')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='cosmos.base.abci.v1beta1.ABCIMessageLog.log', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='cosmos.base.abci.v1beta1.ABCIMessageLog.events', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\014StringEvents\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\200\334 \001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=651,
)


_STRINGEVENT = _descriptor.Descriptor(
  name='StringEvent',
  full_name='cosmos.base.abci.v1beta1.StringEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='cosmos.base.abci.v1beta1.StringEvent.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='cosmos.base.abci.v1beta1.StringEvent.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\200\334 \001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=653,
  serialized_end=749,
)


_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='cosmos.base.abci.v1beta1.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cosmos.base.abci.v1beta1.Attribute.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='cosmos.base.abci.v1beta1.Attribute.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=751,
  serialized_end=790,
)


_GASINFO = _descriptor.Descriptor(
  name='GasInfo',
  full_name='cosmos.base.abci.v1beta1.GasInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gas_wanted', full_name='cosmos.base.abci.v1beta1.GasInfo.gas_wanted', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_used', full_name='cosmos.base.abci.v1beta1.GasInfo.gas_used', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=792,
  serialized_end=839,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='cosmos.base.abci.v1beta1.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='cosmos.base.abci.v1beta1.Result.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='cosmos.base.abci.v1beta1.Result.log', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='cosmos.base.abci.v1beta1.Result.events', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_responses', full_name='cosmos.base.abci.v1beta1.Result.msg_responses', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=842,
  serialized_end=978,
)


_SIMULATIONRESPONSE = _descriptor.Descriptor(
  name='SimulationResponse',
  full_name='cosmos.base.abci.v1beta1.SimulationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gas_info', full_name='cosmos.base.abci.v1beta1.SimulationResponse.gas_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\320\336\037\001\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='cosmos.base.abci.v1beta1.SimulationResponse.result', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=981,
  serialized_end=1114,
)


_MSGDATA = _descriptor.Descriptor(
  name='MsgData',
  full_name='cosmos.base.abci.v1beta1.MsgData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='cosmos.base.abci.v1beta1.MsgData.msg_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cosmos.base.abci.v1beta1.MsgData.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\030\001\200\334 \001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1116,
  serialized_end=1165,
)


_TXMSGDATA = _descriptor.Descriptor(
  name='TxMsgData',
  full_name='cosmos.base.abci.v1beta1.TxMsgData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='cosmos.base.abci.v1beta1.TxMsgData.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_responses', full_name='cosmos.base.abci.v1beta1.TxMsgData.msg_responses', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\200\334 \001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1167,
  serialized_end=1282,
)


_SEARCHTXSRESULT = _descriptor.Descriptor(
  name='SearchTxsResult',
  full_name='cosmos.base.abci.v1beta1.SearchTxsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_count', full_name='cosmos.base.abci.v1beta1.SearchTxsResult.total_count', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='cosmos.base.abci.v1beta1.SearchTxsResult.count', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_number', full_name='cosmos.base.abci.v1beta1.SearchTxsResult.page_number', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_total', full_name='cosmos.base.abci.v1beta1.SearchTxsResult.page_total', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='cosmos.base.abci.v1beta1.SearchTxsResult.limit', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txs', full_name='cosmos.base.abci.v1beta1.SearchTxsResult.txs', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\200\334 \001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1285,
  serialized_end=1451,
)

_TXRESPONSE.fields_by_name['logs'].message_type = _ABCIMESSAGELOG
_TXRESPONSE.fields_by_name['tx'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_TXRESPONSE.fields_by_name['events'].message_type = tendermint_dot_abci_dot_types__pb2._EVENT
_ABCIMESSAGELOG.fields_by_name['events'].message_type = _STRINGEVENT
_STRINGEVENT.fields_by_name['attributes'].message_type = _ATTRIBUTE
_RESULT.fields_by_name['events'].message_type = tendermint_dot_abci_dot_types__pb2._EVENT
_RESULT.fields_by_name['msg_responses'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_SIMULATIONRESPONSE.fields_by_name['gas_info'].message_type = _GASINFO
_SIMULATIONRESPONSE.fields_by_name['result'].message_type = _RESULT
_TXMSGDATA.fields_by_name['data'].message_type = _MSGDATA
_TXMSGDATA.fields_by_name['msg_responses'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_SEARCHTXSRESULT.fields_by_name['txs'].message_type = _TXRESPONSE
DESCRIPTOR.message_types_by_name['TxResponse'] = _TXRESPONSE
DESCRIPTOR.message_types_by_name['ABCIMessageLog'] = _ABCIMESSAGELOG
DESCRIPTOR.message_types_by_name['StringEvent'] = _STRINGEVENT
DESCRIPTOR.message_types_by_name['Attribute'] = _ATTRIBUTE
DESCRIPTOR.message_types_by_name['GasInfo'] = _GASINFO
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['SimulationResponse'] = _SIMULATIONRESPONSE
DESCRIPTOR.message_types_by_name['MsgData'] = _MSGDATA
DESCRIPTOR.message_types_by_name['TxMsgData'] = _TXMSGDATA
DESCRIPTOR.message_types_by_name['SearchTxsResult'] = _SEARCHTXSRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TxResponse = _reflection.GeneratedProtocolMessageType('TxResponse', (_message.Message,), dict(
  DESCRIPTOR = _TXRESPONSE,
  __module__ = 'cosmos.base.abci.v1beta1.abci_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.TxResponse)
  ))
_sym_db.RegisterMessage(TxResponse)

ABCIMessageLog = _reflection.GeneratedProtocolMessageType('ABCIMessageLog', (_message.Message,), dict(
  DESCRIPTOR = _ABCIMESSAGELOG,
  __module__ = 'cosmos.base.abci.v1beta1.abci_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.ABCIMessageLog)
  ))
_sym_db.RegisterMessage(ABCIMessageLog)

StringEvent = _reflection.GeneratedProtocolMessageType('StringEvent', (_message.Message,), dict(
  DESCRIPTOR = _STRINGEVENT,
  __module__ = 'cosmos.base.abci.v1beta1.abci_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.StringEvent)
  ))
_sym_db.RegisterMessage(StringEvent)

Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), dict(
  DESCRIPTOR = _ATTRIBUTE,
  __module__ = 'cosmos.base.abci.v1beta1.abci_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.Attribute)
  ))
_sym_db.RegisterMessage(Attribute)

GasInfo = _reflection.GeneratedProtocolMessageType('GasInfo', (_message.Message,), dict(
  DESCRIPTOR = _GASINFO,
  __module__ = 'cosmos.base.abci.v1beta1.abci_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.GasInfo)
  ))
_sym_db.RegisterMessage(GasInfo)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'cosmos.base.abci.v1beta1.abci_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.Result)
  ))
_sym_db.RegisterMessage(Result)

SimulationResponse = _reflection.GeneratedProtocolMessageType('SimulationResponse', (_message.Message,), dict(
  DESCRIPTOR = _SIMULATIONRESPONSE,
  __module__ = 'cosmos.base.abci.v1beta1.abci_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.SimulationResponse)
  ))
_sym_db.RegisterMessage(SimulationResponse)

MsgData = _reflection.GeneratedProtocolMessageType('MsgData', (_message.Message,), dict(
  DESCRIPTOR = _MSGDATA,
  __module__ = 'cosmos.base.abci.v1beta1.abci_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.MsgData)
  ))
_sym_db.RegisterMessage(MsgData)

TxMsgData = _reflection.GeneratedProtocolMessageType('TxMsgData', (_message.Message,), dict(
  DESCRIPTOR = _TXMSGDATA,
  __module__ = 'cosmos.base.abci.v1beta1.abci_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.TxMsgData)
  ))
_sym_db.RegisterMessage(TxMsgData)

SearchTxsResult = _reflection.GeneratedProtocolMessageType('SearchTxsResult', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHTXSRESULT,
  __module__ = 'cosmos.base.abci.v1beta1.abci_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.SearchTxsResult)
  ))
_sym_db.RegisterMessage(SearchTxsResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\"github.com/cosmos/cosmos-sdk/types\330\341\036\000'))
_TXRESPONSE.fields_by_name['txhash'].has_options = True
_TXRESPONSE.fields_by_name['txhash']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\006TxHash'))
_TXRESPONSE.fields_by_name['logs'].has_options = True
_TXRESPONSE.fields_by_name['logs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\017ABCIMessageLogs\310\336\037\000'))
_TXRESPONSE.fields_by_name['events'].has_options = True
_TXRESPONSE.fields_by_name['events']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_TXRESPONSE.has_options = True
_TXRESPONSE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000'))
_ABCIMESSAGELOG.fields_by_name['msg_index'].has_options = True
_ABCIMESSAGELOG.fields_by_name['msg_index']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\352\336\037\tmsg_index'))
_ABCIMESSAGELOG.fields_by_name['events'].has_options = True
_ABCIMESSAGELOG.fields_by_name['events']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\252\337\037\014StringEvents\310\336\037\000'))
_ABCIMESSAGELOG.has_options = True
_ABCIMESSAGELOG._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\200\334 \001'))
_STRINGEVENT.fields_by_name['attributes'].has_options = True
_STRINGEVENT.fields_by_name['attributes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_STRINGEVENT.has_options = True
_STRINGEVENT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\200\334 \001'))
_RESULT.fields_by_name['data'].has_options = True
_RESULT.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_RESULT.fields_by_name['events'].has_options = True
_RESULT.fields_by_name['events']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_RESULT.has_options = True
_RESULT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000'))
_SIMULATIONRESPONSE.fields_by_name['gas_info'].has_options = True
_SIMULATIONRESPONSE.fields_by_name['gas_info']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\320\336\037\001\310\336\037\000'))
_MSGDATA.has_options = True
_MSGDATA._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\030\001\200\334 \001'))
_TXMSGDATA.fields_by_name['data'].has_options = True
_TXMSGDATA.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_TXMSGDATA.has_options = True
_TXMSGDATA._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\200\334 \001'))
_SEARCHTXSRESULT.has_options = True
_SEARCHTXSRESULT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\200\334 \001'))
# @@protoc_insertion_point(module_scope)
