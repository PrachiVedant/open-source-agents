from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id:str
    message:str
    agent_config:dict

class ChatResponse(BaseModel):
    response: str