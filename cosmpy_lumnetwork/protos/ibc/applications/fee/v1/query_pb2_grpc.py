# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ibc.applications.fee.v1 import query_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2


class QueryStub(object):
  """Query defines the ICS29 gRPC querier service.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.IncentivizedPackets = channel.unary_unary(
        '/ibc.applications.fee.v1.Query/IncentivizedPackets',
        request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsRequest.SerializeToString,
        response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsResponse.FromString,
        )
    self.IncentivizedPacket = channel.unary_unary(
        '/ibc.applications.fee.v1.Query/IncentivizedPacket',
        request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketRequest.SerializeToString,
        response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketResponse.FromString,
        )
    self.IncentivizedPacketsForChannel = channel.unary_unary(
        '/ibc.applications.fee.v1.Query/IncentivizedPacketsForChannel',
        request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsForChannelRequest.SerializeToString,
        response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsForChannelResponse.FromString,
        )
    self.TotalRecvFees = channel.unary_unary(
        '/ibc.applications.fee.v1.Query/TotalRecvFees',
        request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalRecvFeesRequest.SerializeToString,
        response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalRecvFeesResponse.FromString,
        )
    self.TotalAckFees = channel.unary_unary(
        '/ibc.applications.fee.v1.Query/TotalAckFees',
        request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalAckFeesRequest.SerializeToString,
        response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalAckFeesResponse.FromString,
        )
    self.TotalTimeoutFees = channel.unary_unary(
        '/ibc.applications.fee.v1.Query/TotalTimeoutFees',
        request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalTimeoutFeesRequest.SerializeToString,
        response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalTimeoutFeesResponse.FromString,
        )
    self.Payee = channel.unary_unary(
        '/ibc.applications.fee.v1.Query/Payee',
        request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryPayeeRequest.SerializeToString,
        response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryPayeeResponse.FromString,
        )
    self.CounterpartyPayee = channel.unary_unary(
        '/ibc.applications.fee.v1.Query/CounterpartyPayee',
        request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryCounterpartyPayeeRequest.SerializeToString,
        response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryCounterpartyPayeeResponse.FromString,
        )
    self.FeeEnabledChannels = channel.unary_unary(
        '/ibc.applications.fee.v1.Query/FeeEnabledChannels',
        request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelsRequest.SerializeToString,
        response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelsResponse.FromString,
        )
    self.FeeEnabledChannel = channel.unary_unary(
        '/ibc.applications.fee.v1.Query/FeeEnabledChannel',
        request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelRequest.SerializeToString,
        response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelResponse.FromString,
        )


class QueryServicer(object):
  """Query defines the ICS29 gRPC querier service.
  """

  def IncentivizedPackets(self, request, context):
    """IncentivizedPackets returns all incentivized packets and their associated fees
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IncentivizedPacket(self, request, context):
    """IncentivizedPacket returns all packet fees for a packet given its identifier
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IncentivizedPacketsForChannel(self, request, context):
    """Gets all incentivized packets for a specific channel
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TotalRecvFees(self, request, context):
    """TotalRecvFees returns the total receive fees for a packet given its identifier
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TotalAckFees(self, request, context):
    """TotalAckFees returns the total acknowledgement fees for a packet given its identifier
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TotalTimeoutFees(self, request, context):
    """TotalTimeoutFees returns the total timeout fees for a packet given its identifier
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Payee(self, request, context):
    """Payee returns the registered payee address for a specific channel given the relayer address
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CounterpartyPayee(self, request, context):
    """CounterpartyPayee returns the registered counterparty payee for forward relaying
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FeeEnabledChannels(self, request, context):
    """FeeEnabledChannels returns a list of all fee enabled channels
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FeeEnabledChannel(self, request, context):
    """FeeEnabledChannel returns true if the provided port and channel identifiers belong to a fee enabled channel
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'IncentivizedPackets': grpc.unary_unary_rpc_method_handler(
          servicer.IncentivizedPackets,
          request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsRequest.FromString,
          response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsResponse.SerializeToString,
      ),
      'IncentivizedPacket': grpc.unary_unary_rpc_method_handler(
          servicer.IncentivizedPacket,
          request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketRequest.FromString,
          response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketResponse.SerializeToString,
      ),
      'IncentivizedPacketsForChannel': grpc.unary_unary_rpc_method_handler(
          servicer.IncentivizedPacketsForChannel,
          request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsForChannelRequest.FromString,
          response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryIncentivizedPacketsForChannelResponse.SerializeToString,
      ),
      'TotalRecvFees': grpc.unary_unary_rpc_method_handler(
          servicer.TotalRecvFees,
          request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalRecvFeesRequest.FromString,
          response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalRecvFeesResponse.SerializeToString,
      ),
      'TotalAckFees': grpc.unary_unary_rpc_method_handler(
          servicer.TotalAckFees,
          request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalAckFeesRequest.FromString,
          response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalAckFeesResponse.SerializeToString,
      ),
      'TotalTimeoutFees': grpc.unary_unary_rpc_method_handler(
          servicer.TotalTimeoutFees,
          request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalTimeoutFeesRequest.FromString,
          response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryTotalTimeoutFeesResponse.SerializeToString,
      ),
      'Payee': grpc.unary_unary_rpc_method_handler(
          servicer.Payee,
          request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryPayeeRequest.FromString,
          response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryPayeeResponse.SerializeToString,
      ),
      'CounterpartyPayee': grpc.unary_unary_rpc_method_handler(
          servicer.CounterpartyPayee,
          request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryCounterpartyPayeeRequest.FromString,
          response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryCounterpartyPayeeResponse.SerializeToString,
      ),
      'FeeEnabledChannels': grpc.unary_unary_rpc_method_handler(
          servicer.FeeEnabledChannels,
          request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelsRequest.FromString,
          response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelsResponse.SerializeToString,
      ),
      'FeeEnabledChannel': grpc.unary_unary_rpc_method_handler(
          servicer.FeeEnabledChannel,
          request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelRequest.FromString,
          response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_query__pb2.QueryFeeEnabledChannelResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ibc.applications.fee.v1.Query', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
