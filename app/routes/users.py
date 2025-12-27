from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/users", tags=["Users"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.get("/me")
def get_me(token: str = Depends(oauth2_scheme)):
    return {
        "message": "Authenticated request successful",
        "token": token
    }
