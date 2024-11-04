from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.models.users import User


router = APIRouter()


@router.get("")
def list_users(current_user: User = Depends(get_current_user),db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/students")
def list_students(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(User).filter(User.role == "0").all()