from fastapi import FastAPI
from app.routers import auth, books,users,bookings
from app.dependencies.db import Base, engine
app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")
app.include_router(books.router, prefix="/api/v1/books")
app.include_router(users.router,prefix="/api/v1/users")
app.include_router(bookings.router,prefix="/api/v1/bookings")