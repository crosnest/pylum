# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from c4echain.cfesignature import tx_pb2 as c4echain_dot_cfesignature_dot_tx__pb2


class MsgStub(object):
    """Msg defines the Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StoreSignature = channel.unary_unary(
                '/chain4energy.c4echain.cfesignature.Msg/StoreSignature',
                request_serializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgStoreSignature.SerializeToString,
                response_deserializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgStoreSignatureResponse.FromString,
                )
        self.PublishReferencePayloadLink = channel.unary_unary(
                '/chain4energy.c4echain.cfesignature.Msg/PublishReferencePayloadLink',
                request_serializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgPublishReferencePayloadLink.SerializeToString,
                response_deserializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgPublishReferencePayloadLinkResponse.FromString,
                )
        self.CreateAccount = channel.unary_unary(
                '/chain4energy.c4echain.cfesignature.Msg/CreateAccount',
                request_serializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgCreateAccount.SerializeToString,
                response_deserializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgCreateAccountResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the Msg service.
    """

    def StoreSignature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishReferencePayloadLink(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAccount(self, request, context):
        """this line is used by starport scaffolding # proto/tx/rpc
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StoreSignature': grpc.unary_unary_rpc_method_handler(
                    servicer.StoreSignature,
                    request_deserializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgStoreSignature.FromString,
                    response_serializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgStoreSignatureResponse.SerializeToString,
            ),
            'PublishReferencePayloadLink': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishReferencePayloadLink,
                    request_deserializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgPublishReferencePayloadLink.FromString,
                    response_serializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgPublishReferencePayloadLinkResponse.SerializeToString,
            ),
            'CreateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAccount,
                    request_deserializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgCreateAccount.FromString,
                    response_serializer=c4echain_dot_cfesignature_dot_tx__pb2.MsgCreateAccountResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chain4energy.c4echain.cfesignature.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the Msg service.
    """

    @staticmethod
    def StoreSignature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chain4energy.c4echain.cfesignature.Msg/StoreSignature',
            c4echain_dot_cfesignature_dot_tx__pb2.MsgStoreSignature.SerializeToString,
            c4echain_dot_cfesignature_dot_tx__pb2.MsgStoreSignatureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishReferencePayloadLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chain4energy.c4echain.cfesignature.Msg/PublishReferencePayloadLink',
            c4echain_dot_cfesignature_dot_tx__pb2.MsgPublishReferencePayloadLink.SerializeToString,
            c4echain_dot_cfesignature_dot_tx__pb2.MsgPublishReferencePayloadLinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chain4energy.c4echain.cfesignature.Msg/CreateAccount',
            c4echain_dot_cfesignature_dot_tx__pb2.MsgCreateAccount.SerializeToString,
            c4echain_dot_cfesignature_dot_tx__pb2.MsgCreateAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
