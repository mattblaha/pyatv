"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class RegisterHIDDeviceResultMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERRORCODE_FIELD_NUMBER: builtins.int
    DEVICEIDENTIFIER_FIELD_NUMBER: builtins.int
    errorCode: builtins.int
    deviceIdentifier: builtins.int
    def __init__(self,
        *,
        errorCode: typing.Optional[builtins.int] = ...,
        deviceIdentifier: typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["deviceIdentifier",b"deviceIdentifier","errorCode",b"errorCode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deviceIdentifier",b"deviceIdentifier","errorCode",b"errorCode"]) -> None: ...
global___RegisterHIDDeviceResultMessage = RegisterHIDDeviceResultMessage

REGISTERHIDDEVICERESULTMESSAGE_FIELD_NUMBER: builtins.int
registerHIDDeviceResultMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___RegisterHIDDeviceResultMessage]
