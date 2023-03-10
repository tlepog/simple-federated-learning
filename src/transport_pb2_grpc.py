# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import transport_pb2 as transport__pb2


class FederatedAppStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EstablishConnection = channel.unary_unary(
                '/FederatedApp/EstablishConnection',
                request_serializer=transport__pb2.Info.SerializeToString,
                response_deserializer=transport__pb2.Empty.FromString,
                )
        self.Train = channel.unary_unary(
                '/FederatedApp/Train',
                request_serializer=transport__pb2.Empty.SerializeToString,
                response_deserializer=transport__pb2.Message.FromString,
                )
        self.GetParameters = channel.unary_stream(
                '/FederatedApp/GetParameters',
                request_serializer=transport__pb2.Empty.SerializeToString,
                response_deserializer=transport__pb2.Chunk.FromString,
                )
        self.SetParameters = channel.stream_unary(
                '/FederatedApp/SetParameters',
                request_serializer=transport__pb2.Chunk.SerializeToString,
                response_deserializer=transport__pb2.Empty.FromString,
                )
        self.Evaluate = channel.unary_unary(
                '/FederatedApp/Evaluate',
                request_serializer=transport__pb2.Empty.SerializeToString,
                response_deserializer=transport__pb2.Empty.FromString,
                )


class FederatedAppServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EstablishConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Train(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetParameters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetParameters(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Evaluate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FederatedAppServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EstablishConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.EstablishConnection,
                    request_deserializer=transport__pb2.Info.FromString,
                    response_serializer=transport__pb2.Empty.SerializeToString,
            ),
            'Train': grpc.unary_unary_rpc_method_handler(
                    servicer.Train,
                    request_deserializer=transport__pb2.Empty.FromString,
                    response_serializer=transport__pb2.Message.SerializeToString,
            ),
            'GetParameters': grpc.unary_stream_rpc_method_handler(
                    servicer.GetParameters,
                    request_deserializer=transport__pb2.Empty.FromString,
                    response_serializer=transport__pb2.Chunk.SerializeToString,
            ),
            'SetParameters': grpc.stream_unary_rpc_method_handler(
                    servicer.SetParameters,
                    request_deserializer=transport__pb2.Chunk.FromString,
                    response_serializer=transport__pb2.Empty.SerializeToString,
            ),
            'Evaluate': grpc.unary_unary_rpc_method_handler(
                    servicer.Evaluate,
                    request_deserializer=transport__pb2.Empty.FromString,
                    response_serializer=transport__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FederatedApp', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FederatedApp(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EstablishConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederatedApp/EstablishConnection',
            transport__pb2.Info.SerializeToString,
            transport__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Train(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederatedApp/Train',
            transport__pb2.Empty.SerializeToString,
            transport__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetParameters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/FederatedApp/GetParameters',
            transport__pb2.Empty.SerializeToString,
            transport__pb2.Chunk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetParameters(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/FederatedApp/SetParameters',
            transport__pb2.Chunk.SerializeToString,
            transport__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Evaluate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederatedApp/Evaluate',
            transport__pb2.Empty.SerializeToString,
            transport__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
