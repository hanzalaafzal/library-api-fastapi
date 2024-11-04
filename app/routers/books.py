
#import required dependencies
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.middlewares import access_role

#import models
from app.models.books import Book
from app.models.book_categories import BookCategory
from app.models.users import User

#import schemas
from app.schemas.books import BookCreate, BookUpdate


router = APIRouter()

#route to list all the books in 
#this can be accessed by both (student "0" and library worker/admin "1")
@router.get("")
def list_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


#route to list details of book of single 
#this can be accessed by both (student "0" and library worker/admin "1")
@router.get("/{book_id}",description="Fetch list of available books.")
def get_book(book_id: int, db: Session = Depends(get_db)):
    
    book = db.query(Book).filter(Book.id == book_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

#route to create a book
#this can only be accessed by library worker
@router.post("", dependencies=[Depends(access_role.is_library_worker)],description="Add new books. This API requires admin role ")
def add_book(book: BookCreate,
             current_user: User = Depends(get_current_user), 
             db: Session = Depends(get_db)):
    
    new_book = Book(title=book.title, author_id=book.author_id,
                    released_on=book.released_on,slug=book.slug,
                    version=book.version,description=book.description,
                    created_at=book.created_at)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return new_book

#route to update book details
#this can only be accessed by library worker
@router.put("/{book_id}",dependencies=[Depends(access_role.is_library_worker)],description="Update a book. This API requires admin role ")
def update_book(book_id: int, book: BookUpdate, 
                current_user: User = Depends(get_current_user), 
                db: Session = Depends(get_db)):
    
    existing_book = db.query(Book).filter(Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    existing_book.title = book.title or existing_book.title
    db.commit()
    db.refresh(existing_book)
    return existing_book


@router.get("/categories",description="Fetch book category list.")
def list_book_category(db:Session = Depends(get_db)):
    return db.query(BookCategory).all()






