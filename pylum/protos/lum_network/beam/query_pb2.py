# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lum-network/beam/query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from lum_network.beam import beam_pb2 as lum__network_dot_beam_dot_beam__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lum-network/beam/query.proto',
  package='lum.network.beam',
  syntax='proto3',
  serialized_pb=_b('\n\x1clum-network/beam/query.proto\x12\x10lum.network.beam\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1blum-network/beam/beam.proto\"!\n\x13QueryGetBeamRequest\x12\n\n\x02id\x18\x01 \x01(\t\"<\n\x14QueryGetBeamResponse\x12$\n\x04\x62\x65\x61m\x18\x01 \x01(\x0b\x32\x16.lum.network.beam.Beam\"\x80\x01\n\x16QueryFetchBeamsRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x12*\n\x05state\x18\x02 \x01(\x0e\x32\x1b.lum.network.beam.BeamState\"}\n\x17QueryFetchBeamsResponse\x12%\n\x05\x62\x65\x61ms\x18\x01 \x03(\x0b\x32\x16.lum.network.beam.Beam\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"]\n\x1fQueryFetchBeamsOpenQueueRequest\x12:\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"q\n QueryFetchBeamsOpenQueueResponse\x12\x10\n\x08\x62\x65\x61m_ids\x18\x01 \x03(\t\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\x9a\x03\n\x05Query\x12v\n\x04\x42\x65\x61m\x12%.lum.network.beam.QueryGetBeamRequest\x1a&.lum.network.beam.QueryGetBeamResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/lum-network/beams/{id}\x12x\n\x05\x42\x65\x61ms\x12(.lum.network.beam.QueryFetchBeamsRequest\x1a).lum.network.beam.QueryFetchBeamsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/lum-network/beams\x12\x9e\x01\n\x0e\x42\x65\x61msOpenQueue\x12\x31.lum.network.beam.QueryFetchBeamsOpenQueueRequest\x1a\x32.lum.network.beam.QueryFetchBeamsOpenQueueResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/lum-network/beams-open-queueB+Z)github.com/lum-network/chain/x/beam/typesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,lum__network_dot_beam_dot_beam__pb2.DESCRIPTOR,])




_QUERYGETBEAMREQUEST = _descriptor.Descriptor(
  name='QueryGetBeamRequest',
  full_name='lum.network.beam.QueryGetBeamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='lum.network.beam.QueryGetBeamRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=153,
  serialized_end=186,
)


_QUERYGETBEAMRESPONSE = _descriptor.Descriptor(
  name='QueryGetBeamResponse',
  full_name='lum.network.beam.QueryGetBeamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='beam', full_name='lum.network.beam.QueryGetBeamResponse.beam', index=0,
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
  ],
  serialized_start=188,
  serialized_end=248,
)


_QUERYFETCHBEAMSREQUEST = _descriptor.Descriptor(
  name='QueryFetchBeamsRequest',
  full_name='lum.network.beam.QueryFetchBeamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='lum.network.beam.QueryFetchBeamsRequest.pagination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='lum.network.beam.QueryFetchBeamsRequest.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=251,
  serialized_end=379,
)


_QUERYFETCHBEAMSRESPONSE = _descriptor.Descriptor(
  name='QueryFetchBeamsResponse',
  full_name='lum.network.beam.QueryFetchBeamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='beams', full_name='lum.network.beam.QueryFetchBeamsResponse.beams', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='lum.network.beam.QueryFetchBeamsResponse.pagination', index=1,
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
  serialized_start=381,
  serialized_end=506,
)


_QUERYFETCHBEAMSOPENQUEUEREQUEST = _descriptor.Descriptor(
  name='QueryFetchBeamsOpenQueueRequest',
  full_name='lum.network.beam.QueryFetchBeamsOpenQueueRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='lum.network.beam.QueryFetchBeamsOpenQueueRequest.pagination', index=0,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=508,
  serialized_end=601,
)


_QUERYFETCHBEAMSOPENQUEUERESPONSE = _descriptor.Descriptor(
  name='QueryFetchBeamsOpenQueueResponse',
  full_name='lum.network.beam.QueryFetchBeamsOpenQueueResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='beam_ids', full_name='lum.network.beam.QueryFetchBeamsOpenQueueResponse.beam_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='lum.network.beam.QueryFetchBeamsOpenQueueResponse.pagination', index=1,
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
  serialized_start=603,
  serialized_end=716,
)

_QUERYGETBEAMRESPONSE.fields_by_name['beam'].message_type = lum__network_dot_beam_dot_beam__pb2._BEAM
_QUERYFETCHBEAMSREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYFETCHBEAMSREQUEST.fields_by_name['state'].enum_type = lum__network_dot_beam_dot_beam__pb2._BEAMSTATE
_QUERYFETCHBEAMSRESPONSE.fields_by_name['beams'].message_type = lum__network_dot_beam_dot_beam__pb2._BEAM
_QUERYFETCHBEAMSRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYFETCHBEAMSOPENQUEUEREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYFETCHBEAMSOPENQUEUERESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
DESCRIPTOR.message_types_by_name['QueryGetBeamRequest'] = _QUERYGETBEAMREQUEST
DESCRIPTOR.message_types_by_name['QueryGetBeamResponse'] = _QUERYGETBEAMRESPONSE
DESCRIPTOR.message_types_by_name['QueryFetchBeamsRequest'] = _QUERYFETCHBEAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryFetchBeamsResponse'] = _QUERYFETCHBEAMSRESPONSE
DESCRIPTOR.message_types_by_name['QueryFetchBeamsOpenQueueRequest'] = _QUERYFETCHBEAMSOPENQUEUEREQUEST
DESCRIPTOR.message_types_by_name['QueryFetchBeamsOpenQueueResponse'] = _QUERYFETCHBEAMSOPENQUEUERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryGetBeamRequest = _reflection.GeneratedProtocolMessageType('QueryGetBeamRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYGETBEAMREQUEST,
  __module__ = 'lum_network.beam.query_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.beam.QueryGetBeamRequest)
  ))
_sym_db.RegisterMessage(QueryGetBeamRequest)

QueryGetBeamResponse = _reflection.GeneratedProtocolMessageType('QueryGetBeamResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYGETBEAMRESPONSE,
  __module__ = 'lum_network.beam.query_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.beam.QueryGetBeamResponse)
  ))
_sym_db.RegisterMessage(QueryGetBeamResponse)

QueryFetchBeamsRequest = _reflection.GeneratedProtocolMessageType('QueryFetchBeamsRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYFETCHBEAMSREQUEST,
  __module__ = 'lum_network.beam.query_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.beam.QueryFetchBeamsRequest)
  ))
_sym_db.RegisterMessage(QueryFetchBeamsRequest)

QueryFetchBeamsResponse = _reflection.GeneratedProtocolMessageType('QueryFetchBeamsResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYFETCHBEAMSRESPONSE,
  __module__ = 'lum_network.beam.query_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.beam.QueryFetchBeamsResponse)
  ))
_sym_db.RegisterMessage(QueryFetchBeamsResponse)

QueryFetchBeamsOpenQueueRequest = _reflection.GeneratedProtocolMessageType('QueryFetchBeamsOpenQueueRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYFETCHBEAMSOPENQUEUEREQUEST,
  __module__ = 'lum_network.beam.query_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.beam.QueryFetchBeamsOpenQueueRequest)
  ))
_sym_db.RegisterMessage(QueryFetchBeamsOpenQueueRequest)

QueryFetchBeamsOpenQueueResponse = _reflection.GeneratedProtocolMessageType('QueryFetchBeamsOpenQueueResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYFETCHBEAMSOPENQUEUERESPONSE,
  __module__ = 'lum_network.beam.query_pb2'
  # @@protoc_insertion_point(class_scope:lum.network.beam.QueryFetchBeamsOpenQueueResponse)
  ))
_sym_db.RegisterMessage(QueryFetchBeamsOpenQueueResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/lum-network/chain/x/beam/types'))

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='lum.network.beam.Query',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=719,
  serialized_end=1129,
  methods=[
  _descriptor.MethodDescriptor(
    name='Beam',
    full_name='lum.network.beam.Query.Beam',
    index=0,
    containing_service=None,
    input_type=_QUERYGETBEAMREQUEST,
    output_type=_QUERYGETBEAMRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\031\022\027/lum-network/beams/{id}')),
  ),
  _descriptor.MethodDescriptor(
    name='Beams',
    full_name='lum.network.beam.Query.Beams',
    index=1,
    containing_service=None,
    input_type=_QUERYFETCHBEAMSREQUEST,
    output_type=_QUERYFETCHBEAMSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\024\022\022/lum-network/beams')),
  ),
  _descriptor.MethodDescriptor(
    name='BeamsOpenQueue',
    full_name='lum.network.beam.Query.BeamsOpenQueue',
    index=2,
    containing_service=None,
    input_type=_QUERYFETCHBEAMSOPENQUEUEREQUEST,
    output_type=_QUERYFETCHBEAMSOPENQUEUERESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\037\022\035/lum-network/beams-open-queue')),
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)