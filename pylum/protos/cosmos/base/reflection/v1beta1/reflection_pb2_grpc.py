# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from cosmos.base.reflection.v1beta1 import reflection_pb2 as cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2


class ReflectionServiceStub(object):
  """ReflectionService defines a service for interface reflection.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListAllInterfaces = channel.unary_unary(
        '/cosmos.base.reflection.v1beta1.ReflectionService/ListAllInterfaces',
        request_serializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListAllInterfacesRequest.SerializeToString,
        response_deserializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListAllInterfacesResponse.FromString,
        )
    self.ListImplementations = channel.unary_unary(
        '/cosmos.base.reflection.v1beta1.ReflectionService/ListImplementations',
        request_serializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListImplementationsRequest.SerializeToString,
        response_deserializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListImplementationsResponse.FromString,
        )


class ReflectionServiceServicer(object):
  """ReflectionService defines a service for interface reflection.
  """

  def ListAllInterfaces(self, request, context):
    """ListAllInterfaces lists all the interfaces registered in the interface
    registry.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListImplementations(self, request, context):
    """ListImplementations list all the concrete types that implement a given
    interface.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ReflectionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListAllInterfaces': grpc.unary_unary_rpc_method_handler(
          servicer.ListAllInterfaces,
          request_deserializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListAllInterfacesRequest.FromString,
          response_serializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListAllInterfacesResponse.SerializeToString,
      ),
      'ListImplementations': grpc.unary_unary_rpc_method_handler(
          servicer.ListImplementations,
          request_deserializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListImplementationsRequest.FromString,
          response_serializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListImplementationsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cosmos.base.reflection.v1beta1.ReflectionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))