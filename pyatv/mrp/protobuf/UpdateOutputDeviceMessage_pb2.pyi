# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.Common_pb2 import (
    DeviceSubType as pyatv___mrp___protobuf___Common_pb2___DeviceSubType,
    DeviceType as pyatv___mrp___protobuf___Common_pb2___DeviceType,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class AVOutputDeviceSourceInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    routingContextUID = ... # type: typing___Text
    multipleBuiltInDevices = ... # type: builtin___bool

    def __init__(self,
        *,
        routingContextUID : typing___Optional[typing___Text] = None,
        multipleBuiltInDevices : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AVOutputDeviceSourceInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AVOutputDeviceSourceInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"multipleBuiltInDevices",b"multipleBuiltInDevices",u"routingContextUID",b"routingContextUID"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"multipleBuiltInDevices",b"multipleBuiltInDevices",u"routingContextUID",b"routingContextUID"]) -> None: ...
global___AVOutputDeviceSourceInfo = AVOutputDeviceSourceInfo

class AVOutputDeviceDescriptor(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    uniqueIdentifier = ... # type: typing___Text
    groupID = ... # type: typing___Text
    modelID = ... # type: typing___Text
    macAddress = ... # type: builtin___bytes
    canAccessRemoteAssets = ... # type: builtin___bool
    isRemoteControllable = ... # type: builtin___bool
    isGroupLeader = ... # type: builtin___bool
    isGroupable = ... # type: builtin___bool
    deviceType = ... # type: pyatv___mrp___protobuf___Common_pb2___DeviceType.Enum
    deviceSubType = ... # type: pyatv___mrp___protobuf___Common_pb2___DeviceSubType.Enum
    modelSpecificInfoData = ... # type: builtin___bytes
    batteryLevel = ... # type: builtin___float
    isLocalDevice = ... # type: builtin___bool
    supportsExternalScreen = ... # type: builtin___bool
    requiresAuthorization = ... # type: builtin___bool
    shouldForceRemoteControlabillity = ... # type: builtin___bool
    isDeviceGroupable = ... # type: builtin___bool
    canRelayCommunicationChannel = ... # type: builtin___bool
    logicalDeviceID = ... # type: typing___Text
    isProxyGroupPlayer = ... # type: builtin___bool
    firmwareVersion = ... # type: typing___Text
    volume = ... # type: builtin___float
    isVolumeControlAvailable = ... # type: builtin___bool
    canAccessAppleMusic = ... # type: builtin___bool
    canAccessiCloudMusicLibrary = ... # type: builtin___bool
    groupContainsGroupLeader = ... # type: builtin___bool
    supportsBufferedAirPlay = ... # type: builtin___bool
    canPlayEncryptedProgressiveDownloadAssets = ... # type: builtin___bool
    anFetchMediaDataFromSender = ... # type: builtin___bool
    resentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets = ... # type: builtin___bool
    isAirPlayReceiverSessionActive = ... # type: builtin___bool
    parentGroupIdentifier = ... # type: typing___Text
    parentGroupContainsDiscoverableLeader = ... # type: builtin___bool
    isAddedToHomeKit = ... # type: builtin___bool
    volumeCapabilities = ... # type: builtin___int
    bluetoothID = ... # type: typing___Text

    @property
    def sourceInfo(self) -> global___AVOutputDeviceSourceInfo: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        uniqueIdentifier : typing___Optional[typing___Text] = None,
        groupID : typing___Optional[typing___Text] = None,
        modelID : typing___Optional[typing___Text] = None,
        macAddress : typing___Optional[builtin___bytes] = None,
        canAccessRemoteAssets : typing___Optional[builtin___bool] = None,
        isRemoteControllable : typing___Optional[builtin___bool] = None,
        isGroupLeader : typing___Optional[builtin___bool] = None,
        isGroupable : typing___Optional[builtin___bool] = None,
        deviceType : typing___Optional[pyatv___mrp___protobuf___Common_pb2___DeviceType.Enum] = None,
        deviceSubType : typing___Optional[pyatv___mrp___protobuf___Common_pb2___DeviceSubType.Enum] = None,
        modelSpecificInfoData : typing___Optional[builtin___bytes] = None,
        batteryLevel : typing___Optional[builtin___float] = None,
        isLocalDevice : typing___Optional[builtin___bool] = None,
        supportsExternalScreen : typing___Optional[builtin___bool] = None,
        requiresAuthorization : typing___Optional[builtin___bool] = None,
        shouldForceRemoteControlabillity : typing___Optional[builtin___bool] = None,
        sourceInfo : typing___Optional[global___AVOutputDeviceSourceInfo] = None,
        isDeviceGroupable : typing___Optional[builtin___bool] = None,
        canRelayCommunicationChannel : typing___Optional[builtin___bool] = None,
        logicalDeviceID : typing___Optional[typing___Text] = None,
        isProxyGroupPlayer : typing___Optional[builtin___bool] = None,
        firmwareVersion : typing___Optional[typing___Text] = None,
        volume : typing___Optional[builtin___float] = None,
        isVolumeControlAvailable : typing___Optional[builtin___bool] = None,
        canAccessAppleMusic : typing___Optional[builtin___bool] = None,
        canAccessiCloudMusicLibrary : typing___Optional[builtin___bool] = None,
        groupContainsGroupLeader : typing___Optional[builtin___bool] = None,
        supportsBufferedAirPlay : typing___Optional[builtin___bool] = None,
        canPlayEncryptedProgressiveDownloadAssets : typing___Optional[builtin___bool] = None,
        anFetchMediaDataFromSender : typing___Optional[builtin___bool] = None,
        resentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets : typing___Optional[builtin___bool] = None,
        isAirPlayReceiverSessionActive : typing___Optional[builtin___bool] = None,
        parentGroupIdentifier : typing___Optional[typing___Text] = None,
        parentGroupContainsDiscoverableLeader : typing___Optional[builtin___bool] = None,
        isAddedToHomeKit : typing___Optional[builtin___bool] = None,
        volumeCapabilities : typing___Optional[builtin___int] = None,
        bluetoothID : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AVOutputDeviceDescriptor: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AVOutputDeviceDescriptor: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"anFetchMediaDataFromSender",b"anFetchMediaDataFromSender",u"batteryLevel",b"batteryLevel",u"bluetoothID",b"bluetoothID",u"canAccessAppleMusic",b"canAccessAppleMusic",u"canAccessRemoteAssets",b"canAccessRemoteAssets",u"canAccessiCloudMusicLibrary",b"canAccessiCloudMusicLibrary",u"canPlayEncryptedProgressiveDownloadAssets",b"canPlayEncryptedProgressiveDownloadAssets",u"canRelayCommunicationChannel",b"canRelayCommunicationChannel",u"deviceSubType",b"deviceSubType",u"deviceType",b"deviceType",u"firmwareVersion",b"firmwareVersion",u"groupContainsGroupLeader",b"groupContainsGroupLeader",u"groupID",b"groupID",u"isAddedToHomeKit",b"isAddedToHomeKit",u"isAirPlayReceiverSessionActive",b"isAirPlayReceiverSessionActive",u"isDeviceGroupable",b"isDeviceGroupable",u"isGroupLeader",b"isGroupLeader",u"isGroupable",b"isGroupable",u"isLocalDevice",b"isLocalDevice",u"isProxyGroupPlayer",b"isProxyGroupPlayer",u"isRemoteControllable",b"isRemoteControllable",u"isVolumeControlAvailable",b"isVolumeControlAvailable",u"logicalDeviceID",b"logicalDeviceID",u"macAddress",b"macAddress",u"modelID",b"modelID",u"modelSpecificInfoData",b"modelSpecificInfoData",u"name",b"name",u"parentGroupContainsDiscoverableLeader",b"parentGroupContainsDiscoverableLeader",u"parentGroupIdentifier",b"parentGroupIdentifier",u"requiresAuthorization",b"requiresAuthorization",u"resentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets",b"resentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets",u"shouldForceRemoteControlabillity",b"shouldForceRemoteControlabillity",u"sourceInfo",b"sourceInfo",u"supportsBufferedAirPlay",b"supportsBufferedAirPlay",u"supportsExternalScreen",b"supportsExternalScreen",u"uniqueIdentifier",b"uniqueIdentifier",u"volume",b"volume",u"volumeCapabilities",b"volumeCapabilities"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"anFetchMediaDataFromSender",b"anFetchMediaDataFromSender",u"batteryLevel",b"batteryLevel",u"bluetoothID",b"bluetoothID",u"canAccessAppleMusic",b"canAccessAppleMusic",u"canAccessRemoteAssets",b"canAccessRemoteAssets",u"canAccessiCloudMusicLibrary",b"canAccessiCloudMusicLibrary",u"canPlayEncryptedProgressiveDownloadAssets",b"canPlayEncryptedProgressiveDownloadAssets",u"canRelayCommunicationChannel",b"canRelayCommunicationChannel",u"deviceSubType",b"deviceSubType",u"deviceType",b"deviceType",u"firmwareVersion",b"firmwareVersion",u"groupContainsGroupLeader",b"groupContainsGroupLeader",u"groupID",b"groupID",u"isAddedToHomeKit",b"isAddedToHomeKit",u"isAirPlayReceiverSessionActive",b"isAirPlayReceiverSessionActive",u"isDeviceGroupable",b"isDeviceGroupable",u"isGroupLeader",b"isGroupLeader",u"isGroupable",b"isGroupable",u"isLocalDevice",b"isLocalDevice",u"isProxyGroupPlayer",b"isProxyGroupPlayer",u"isRemoteControllable",b"isRemoteControllable",u"isVolumeControlAvailable",b"isVolumeControlAvailable",u"logicalDeviceID",b"logicalDeviceID",u"macAddress",b"macAddress",u"modelID",b"modelID",u"modelSpecificInfoData",b"modelSpecificInfoData",u"name",b"name",u"parentGroupContainsDiscoverableLeader",b"parentGroupContainsDiscoverableLeader",u"parentGroupIdentifier",b"parentGroupIdentifier",u"requiresAuthorization",b"requiresAuthorization",u"resentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets",b"resentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets",u"shouldForceRemoteControlabillity",b"shouldForceRemoteControlabillity",u"sourceInfo",b"sourceInfo",u"supportsBufferedAirPlay",b"supportsBufferedAirPlay",u"supportsExternalScreen",b"supportsExternalScreen",u"uniqueIdentifier",b"uniqueIdentifier",u"volume",b"volume",u"volumeCapabilities",b"volumeCapabilities"]) -> None: ...
global___AVOutputDeviceDescriptor = AVOutputDeviceDescriptor

class UpdateOutputDeviceMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def outputDevices(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___AVOutputDeviceDescriptor]: ...

    def __init__(self,
        *,
        outputDevices : typing___Optional[typing___Iterable[global___AVOutputDeviceDescriptor]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateOutputDeviceMessage: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateOutputDeviceMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"outputDevices",b"outputDevices"]) -> None: ...
global___UpdateOutputDeviceMessage = UpdateOutputDeviceMessage

updateOutputDeviceMessage = ... # type: google___protobuf___descriptor___FieldDescriptor