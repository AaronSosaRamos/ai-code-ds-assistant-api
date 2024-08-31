from enum import Enum
from typing import Any, List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: str
    fullName: str
    email: str
    
class Role(str, Enum):
    human = "human"
    ai = "ai"
    system = "system"

class MessageType(str, Enum):
    text = "text"
    image = "image"
    video = "video"
    file = "file"

class MessagePayload(BaseModel):
    text: str

class Message(BaseModel):
    role: Role
    type: MessageType
    timestamp: Optional[Any] = None
    payload: MessagePayload

class RequestType(str, Enum):
    chat = "chat"
    tool = "tool"

class ChatMessage(BaseModel):
    role: str
    type: str
    text: str

class GenericRequest(BaseModel):
    user: User
    type: RequestType

class ChatRequest(GenericRequest):
    messages: List[Message]

class ChatResponse(BaseModel):
    data: List[Message]