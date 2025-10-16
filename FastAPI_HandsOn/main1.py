from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

app = FastAPI(title="Book Management API")

class Author(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Author's full name")
    age: Optional[int] = Field(None, gt=0, lt=120, description="Age of the author (optional)")


class Book(BaseModel):
    id: int = Field(..., gt=0, description="Book ID (must be positive)")
    title: str = Field(..., min_length=3, max_length=100, description="Title of the book")
    author: Author
    pages: int = Field(..., gt=0, le=2000, description="Number of pages in the book")
    price: float = Field(..., gt=0, description="Price of the book (must be positive)")
    genre: Optional[str] = Field(None, description="Genre of the book (optional)")

    @field_validator("title")
    def title_must_not_contain_number(cls, value):
        if any(char.isdigit() for char in value):
            raise ValueError("Book title must not contain numbers")
        return value


books_db = [
    Book(id=1,
         title="Harry Potter and the Sorcerer's Stone",
         author=Author(name="J.K.Rowling", age=55),
         pages=309,
         price=499.99,
         genre="Fantasy"),
    Book(id=2,
         title="The Hobbit",
         author=Author(name="J.R.R. Tolkien", age=81),
         pages=310,
         price=399.50,
         genre="Adventure"),
    Book(id=3,
         title="George Book",
         author=Author(name="George Orwell", age=46),
         pages=328,
         price=299.99,
         genre="Dystopian")
]
@app.get("/")
def home():
    return {"message": "Welcome to Book Management API"}

@app.get("/books", response_model=List[Book])
def get_books(author: Optional[str] = None):
    if author:
        filtered_books = [book for book in books_db if book.author.name.lower() == author.lower()]
        return filtered_books
    return books_db

@app.get("/books/{book_id}", response_model=Book)
def get_book_by_id(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def add_book(book: Book):
    for existing_book in books_db:
        if existing_book.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books_db.append(book)
    return book

@app.get("/getAll",response_model=List[Book])
def getAllBooks():
    return books_db