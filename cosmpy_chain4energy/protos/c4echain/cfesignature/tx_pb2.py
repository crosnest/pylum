# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c4echain/cfesignature/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from c4echain.cfesignature import params_pb2 as c4echain_dot_cfesignature_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63\x34\x65\x63hain/cfesignature/tx.proto\x12\"chain4energy.c4echain.cfesignature\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\"c4echain/cfesignature/params.proto\"O\n\x11MsgStoreSignature\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x12\n\nstorageKey\x18\x02 \x01(\t\x12\x15\n\rsignatureJSON\x18\x03 \x01(\t\">\n\x19MsgStoreSignatureResponse\x12\x0c\n\x04txId\x18\x01 \x01(\t\x12\x13\n\x0btxTimestamp\x18\x02 \x01(\t\"M\n\x1eMsgPublishReferencePayloadLink\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"=\n&MsgPublishReferencePayloadLinkResponse\x12\x13\n\x0btxTimestamp\x18\x01 \x01(\t\"S\n\x10MsgCreateAccount\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x18\n\x10\x61\x63\x63\x41\x64\x64ressString\x18\x02 \x01(\t\x12\x14\n\x0cpubKeyString\x18\x03 \x01(\t\"1\n\x18MsgCreateAccountResponse\x12\x15\n\raccountNumber\x18\x01 \x01(\t2\xc4\x03\n\x03Msg\x12\x86\x01\n\x0eStoreSignature\x12\x35.chain4energy.c4echain.cfesignature.MsgStoreSignature\x1a=.chain4energy.c4echain.cfesignature.MsgStoreSignatureResponse\x12\xad\x01\n\x1bPublishReferencePayloadLink\x12\x42.chain4energy.c4echain.cfesignature.MsgPublishReferencePayloadLink\x1aJ.chain4energy.c4echain.cfesignature.MsgPublishReferencePayloadLinkResponse\x12\x83\x01\n\rCreateAccount\x12\x34.chain4energy.c4echain.cfesignature.MsgCreateAccount\x1a<.chain4energy.c4echain.cfesignature.MsgCreateAccountResponseB8Z6github.com/chain4energy/c4e-chain/x/cfesignature/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'c4echain.cfesignature.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6github.com/chain4energy/c4e-chain/x/cfesignature/types'
  _MSGSTORESIGNATURE._serialized_start=180
  _MSGSTORESIGNATURE._serialized_end=259
  _MSGSTORESIGNATURERESPONSE._serialized_start=261
  _MSGSTORESIGNATURERESPONSE._serialized_end=323
  _MSGPUBLISHREFERENCEPAYLOADLINK._serialized_start=325
  _MSGPUBLISHREFERENCEPAYLOADLINK._serialized_end=402
  _MSGPUBLISHREFERENCEPAYLOADLINKRESPONSE._serialized_start=404
  _MSGPUBLISHREFERENCEPAYLOADLINKRESPONSE._serialized_end=465
  _MSGCREATEACCOUNT._serialized_start=467
  _MSGCREATEACCOUNT._serialized_end=550
  _MSGCREATEACCOUNTRESPONSE._serialized_start=552
  _MSGCREATEACCOUNTRESPONSE._serialized_end=601
  _MSG._serialized_start=604
  _MSG._serialized_end=1056
# @@protoc_insertion_point(module_scope)
