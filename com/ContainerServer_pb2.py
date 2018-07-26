# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ContainerServer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ContainerServer.proto',
  package='testpythonwithjava',
  syntax='proto3',
  serialized_pb=_b('\n\x15\x43ontainerServer.proto\x12\x12testpythonwithjava\"4\n\nDockerInfo\x12\x10\n\x08\x64ockerip\x18\x01 \x01(\t\x12\x14\n\x0c\x64ockerstatus\x18\x02 \x01(\t\"P\n\x06\x44ocker\x12\x12\n\ndockername\x18\x01 \x01(\t\x12\x32\n\ndockerinfo\x18\x02 \x01(\x0b\x32\x1e.testpythonwithjava.DockerInfo\"P\n\tContainer\x12\x13\n\x0b\x63ontainerip\x18\x01 \x01(\t\x12.\n\ndockerlist\x18\x02 \x03(\x0b\x32\x1a.testpythonwithjava.Docker\"E\n\rContainerList\x12\x34\n\rcontainerlist\x18\x01 \x03(\x0b\x32\x1d.testpythonwithjava.Container\"\n\n\x08Response2b\n\x11SentServiceStatus\x12M\n\x08\x63ontlist\x12!.testpythonwithjava.ContainerList\x1a\x1c.testpythonwithjava.Response\"\x00\x42\x02P\x01\x62\x06proto3')
)




_DOCKERINFO = _descriptor.Descriptor(
  name='DockerInfo',
  full_name='testpythonwithjava.DockerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dockerip', full_name='testpythonwithjava.DockerInfo.dockerip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dockerstatus', full_name='testpythonwithjava.DockerInfo.dockerstatus', index=1,
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
  serialized_start=45,
  serialized_end=97,
)


_DOCKER = _descriptor.Descriptor(
  name='Docker',
  full_name='testpythonwithjava.Docker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dockername', full_name='testpythonwithjava.Docker.dockername', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dockerinfo', full_name='testpythonwithjava.Docker.dockerinfo', index=1,
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
  serialized_start=99,
  serialized_end=179,
)


_CONTAINER = _descriptor.Descriptor(
  name='Container',
  full_name='testpythonwithjava.Container',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='containerip', full_name='testpythonwithjava.Container.containerip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dockerlist', full_name='testpythonwithjava.Container.dockerlist', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=261,
)


_CONTAINERLIST = _descriptor.Descriptor(
  name='ContainerList',
  full_name='testpythonwithjava.ContainerList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='containerlist', full_name='testpythonwithjava.ContainerList.containerlist', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=263,
  serialized_end=332,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='testpythonwithjava.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=334,
  serialized_end=344,
)

_DOCKER.fields_by_name['dockerinfo'].message_type = _DOCKERINFO
_CONTAINER.fields_by_name['dockerlist'].message_type = _DOCKER
_CONTAINERLIST.fields_by_name['containerlist'].message_type = _CONTAINER
DESCRIPTOR.message_types_by_name['DockerInfo'] = _DOCKERINFO
DESCRIPTOR.message_types_by_name['Docker'] = _DOCKER
DESCRIPTOR.message_types_by_name['Container'] = _CONTAINER
DESCRIPTOR.message_types_by_name['ContainerList'] = _CONTAINERLIST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DockerInfo = _reflection.GeneratedProtocolMessageType('DockerInfo', (_message.Message,), dict(
  DESCRIPTOR = _DOCKERINFO,
  __module__ = 'ContainerServer_pb2'
  # @@protoc_insertion_point(class_scope:testpythonwithjava.DockerInfo)
  ))
_sym_db.RegisterMessage(DockerInfo)

Docker = _reflection.GeneratedProtocolMessageType('Docker', (_message.Message,), dict(
  DESCRIPTOR = _DOCKER,
  __module__ = 'ContainerServer_pb2'
  # @@protoc_insertion_point(class_scope:testpythonwithjava.Docker)
  ))
_sym_db.RegisterMessage(Docker)

Container = _reflection.GeneratedProtocolMessageType('Container', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINER,
  __module__ = 'ContainerServer_pb2'
  # @@protoc_insertion_point(class_scope:testpythonwithjava.Container)
  ))
_sym_db.RegisterMessage(Container)

ContainerList = _reflection.GeneratedProtocolMessageType('ContainerList', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINERLIST,
  __module__ = 'ContainerServer_pb2'
  # @@protoc_insertion_point(class_scope:testpythonwithjava.ContainerList)
  ))
_sym_db.RegisterMessage(ContainerList)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'ContainerServer_pb2'
  # @@protoc_insertion_point(class_scope:testpythonwithjava.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))

_SENTSERVICESTATUS = _descriptor.ServiceDescriptor(
  name='SentServiceStatus',
  full_name='testpythonwithjava.SentServiceStatus',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=346,
  serialized_end=444,
  methods=[
  _descriptor.MethodDescriptor(
    name='contlist',
    full_name='testpythonwithjava.SentServiceStatus.contlist',
    index=0,
    containing_service=None,
    input_type=_CONTAINERLIST,
    output_type=_RESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENTSERVICESTATUS)

DESCRIPTOR.services_by_name['SentServiceStatus'] = _SENTSERVICESTATUS

# @@protoc_insertion_point(module_scope)