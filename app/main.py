from fastapi import FastAPI, Depends, HTTPException, status
from app.database import Base, engine

from app.routes.auth import router as auth_router
from app.routes.users import router as user_router
from app.routes.ai_chat import router as ai_router

app = FastAPI(title="FastAPI Auth + AI Chat")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(ai_router)

@app.get("/")
async def health_check():
    return {"status": "running"}
