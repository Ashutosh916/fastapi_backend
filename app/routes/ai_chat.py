from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.schemas.ai_chat import AIGenerateRequest, AIGenerateResponse
from app.utils.ai_client import generate_text

router = APIRouter(prefix="/ai", tags=["AI"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/generate", response_model=AIGenerateResponse)
async def generate_ai_text(
    payload: AIGenerateRequest,
    token: str = Depends(oauth2_scheme)
):
    try:
        reply = await generate_text(payload.prompt)
        return {"reply": reply}
    except Exception:
        raise HTTPException(status_code=500, detail="AI service error")
