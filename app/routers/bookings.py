from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.models.users import User
from app.models.bookings import Booking
from app.middlewares.access_role import is_library_worker
from app.schemas.bookings import BookingCreate


router = APIRouter()

# List all bookings (library worker only)
@router.get("",dependencies=[Depends(is_library_worker)],description="Fetch list of bookings. This API requires admin role ")
def list_bookings(current_user: User = Depends(get_current_user), 
                  db: Session = Depends(get_db)):
    
    return db.query(Booking).all()


#Add a booking (student only)
@router.post("")
def create_booking(booking: BookingCreate, 
                   current_user: User = Depends(get_current_user),
                   db: Session = Depends(get_db)):
    
    new_booking = Booking(book_id=booking.book_id, student_id=current_user.id)
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

# Approve or decline a booking (library worker only)
@router.put("/{booking_id}")
def update_booking(booking_id: int, approved: bool, 
                   current_user: User = Depends(get_current_user), 
                   db: Session = Depends(get_db)):
    
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    booking.approved = approved
    db.commit()
    db.refresh(booking)
    return booking