from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.models.users import User
from app.services.auth import verify_password, create_access_token
from app.schemas.auth import Authentication

router = APIRouter()

@router.post("/login")
def login(credentials: Authentication, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == credentials.email).first()
    
    if not user or not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(email=user.email)
    return {"access_token": access_token, "token_type": "bearer"}