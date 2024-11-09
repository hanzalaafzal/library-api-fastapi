
from typing import List
from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.dependencies.books import BookOperations
from app.dependencies.book_category import BookCategoryOperations
from app.middlewares import access_role
from app.models.users import User
from app.schemas.books import BookCreate, BookUpdate, BookApiResponse, BookResponse


router = APIRouter()

book_operation = BookOperations()
category_operation = BookCategoryOperations()

#route to list all the books in 
#this can be accessed by both (student "0" and library worker/admin "1")

@router.get("",description="Fetch list of available books.",
            response_model = BookApiResponse)
def list_books():
    return book_operation.list_books()

#route to list details of book of single 
#this can be accessed by both (student "0" and library worker/admin "1")

@router.get("/{book_id}",description="Fetch the data against book id.",
            response_model = BookApiResponse)

def get_book(book_id: int):
    return book_operation.list_books(book_id)

#route to create a book
#this can only be accessed by library worker

@router.post("", dependencies=[Depends(access_role.is_library_worker)],
             description="Add new books. This API requires admin role ")

def add_book(book: BookCreate,
             current_user: User = Depends(get_current_user)):
    return book_operation.add_book(book)

#route to update book details
#this can only be accessed by library worker
@router.put("/{book_id}",dependencies=[Depends(access_role.is_library_worker)],
            description="Update a book. This API requires admin role ")

def update_book(book_id: int, book: BookUpdate, 
                current_user: User = Depends(get_current_user)):
    return book_operation.update_book(book_id,book)


@router.get("/categories",description="Fetch book category list.")
def list_book_category():
    return category_operation.get_category()






