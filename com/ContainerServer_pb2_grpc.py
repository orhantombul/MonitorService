# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ContainerServer_pb2 as ContainerServer__pb2


class SentServiceStatusStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.contlist = channel.unary_unary(
        '/testpythonwithjava.SentServiceStatus/contlist',
        request_serializer=ContainerServer__pb2.ContainerList.SerializeToString,
        response_deserializer=ContainerServer__pb2.Response.FromString,
        )


class SentServiceStatusServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def contlist(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SentServiceStatusServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'contlist': grpc.unary_unary_rpc_method_handler(
          servicer.contlist,
          request_deserializer=ContainerServer__pb2.ContainerList.FromString,
          response_serializer=ContainerServer__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'testpythonwithjava.SentServiceStatus', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
