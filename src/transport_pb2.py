# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftransport.proto\"\x1b\n\nParameters\x12\r\n\x05value\x18\x01 \x01(\x0c\"\x16\n\x05\x45mpty\x12\r\n\x05value\x18\x01 \x01(\x05\"(\n\x04Info\x12\x12\n\nnodeNumber\x18\x01 \x01(\x05\x12\x0c\n\x04port\x18\x02 \x01(\x05\"\x17\n\x05\x43hunk\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\x32S\n\x0c\x46\x65\x64\x65ratedApp\x12&\n\x13\x45stablishConnection\x12\x05.Info\x1a\x06.Empty\"\x00\x12\x1b\n\x05Train\x12\x06.Chunk\x1a\x06.Empty\"\x00(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PARAMETERS._serialized_start=19
  _PARAMETERS._serialized_end=46
  _EMPTY._serialized_start=48
  _EMPTY._serialized_end=70
  _INFO._serialized_start=72
  _INFO._serialized_end=112
  _CHUNK._serialized_start=114
  _CHUNK._serialized_end=137
  _FEDERATEDAPP._serialized_start=139
  _FEDERATEDAPP._serialized_end=222
# @@protoc_insertion_point(module_scope)