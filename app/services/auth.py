import bcrypt
from datetime import datetime,timedelta
import jwt
import os

TOKEN_EXPIRE_MINUTES = 60

def hash_password(plain_password: str) -> str:
    return bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def create_access_token(email: str):
    token_data = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    }
    
    return jwt.encode(token_data, os.getenv("AUTH_KEY"), algorithm=os.getenv("ALGORITHM"))