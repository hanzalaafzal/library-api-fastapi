from fastapi import Depends, HTTPException, status
from app.models.users import User
from app.dependencies.auth import get_current_user

def is_student(current_user: User = Depends(get_current_user)):
    if current_user.role != 0:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: Requires student role"
        )

def is_library_worker(current_user: User = Depends(get_current_user)):
    if current_user.role != 1:  
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: Requires library worker/admin role"
        )