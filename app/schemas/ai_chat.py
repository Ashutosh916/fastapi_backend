from pydantic import BaseModel

class AIGenerateRequest(BaseModel):
    prompt: str

class AIGenerateResponse(BaseModel):
    reply: str
