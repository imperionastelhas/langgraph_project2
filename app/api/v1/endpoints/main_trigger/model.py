from typing import Optional, Any, Dict
from pydantic import BaseModel

class MessageData(BaseModel):
    key: Dict[str, Any]
    pushName: Optional[str]
    status: Optional[str]
    message: Dict[str, Any]  # Genérico: aceita texto, áudio, imagem, etc.
    messageType: Optional[str]
    messageTimestamp: Optional[int]
    instanceId: Optional[str]
    source: Optional[str]

class WhatsAppEvent(BaseModel):
    event: str
    instance: str
    data: MessageData
    destination: Optional[str]
    date_time: Optional[str]
    sender: Optional[str]
    server_url: Optional[str]
    apikey: Optional[str]

class TriggerResponse(BaseModel):
    result: str