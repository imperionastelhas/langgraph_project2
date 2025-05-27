from pydantic import BaseModel
# from typing import List, Dict

class TriggerResponse(BaseModel):
    result: str
    
class MessageInput(BaseModel):
    messages: list
