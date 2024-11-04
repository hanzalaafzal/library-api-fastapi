from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.dependencies.db import get_db
from app.models.users import User
import os
import jwt

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                  detail="Could not validate credentials",
                                  headers={"WWW-Authenticate": "Bearer"})
    try:
         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
         email = decoded_token.get("sub")
         if email is None:
             raise exception
         
    except jwt.PyJWTError:
        raise exception
    
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise exception
    
    return user
    