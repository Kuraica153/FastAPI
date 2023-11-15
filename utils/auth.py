import os
from fastapi import Depends, HTTPException, status
from .app_exceptions import AppException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

load_dotenv()

ALGORITHM = os.getenv("ENCRYPTION_ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

def decode_token(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token 
        """ if decoded_token["expires"] >= datetime.utcnow() else None """
    except JWTError:
        return AppException.BadRequest(detail="Session expired")
    
def get_current_user(token: str = Depends(oauth2_scheme)):
    user_id = decode_token(token)
    if user_id is None:
        raise AppException.Unauthorized(detail="Session expired")
    return user_id

def signJWT(user_id: str) -> Dict[str, Any]:
    payload = {
        "user_id": user_id,
        "expires": f'{datetime.utcnow() + access_token_expires}'
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token