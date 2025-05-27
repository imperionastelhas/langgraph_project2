from pydantic import BaseModel, RootModel
from typing import List, Optional, Dict, Any

class TriggerResponse(BaseModel):
    result: str
    
class MessageInput(BaseModel):
    messages: list

class Key(BaseModel):
    remoteJid: str
    fromMe: bool
    id: str


class DeviceListMetadata(BaseModel):
    senderKeyHash: str
    senderTimestamp: str
    recipientKeyHash: str
    recipientTimestamp: str


class MessageContextInfo(BaseModel):
    deviceListMetadata: DeviceListMetadata
    deviceListMetadataVersion: int
    messageSecret: str


class MessageContent(BaseModel):
    conversation: Optional[str]
    messageContextInfo: Optional[MessageContextInfo]


class DataPayload(BaseModel):
    key: Key
    pushName: str
    status: str
    message: MessageContent
    messageType: str
    messageTimestamp: int
    instanceId: str
    source: str


class BodyPayload(BaseModel):
    event: str
    instance: str
    data: DataPayload
    destination: str
    date_time: str
    sender: str
    server_url: str
    apikey: str


class WebhookRequest(BaseModel):
    headers: Dict[str, Any]
    params: Dict[str, Any]
    query: Dict[str, Any]
    body: BodyPayload
    webhookUrl: str
    executionMode: str


# Esse é o formato principal que será recebido
class WebhookRequestList(RootModel[List[WebhookRequest]]):
    pass
