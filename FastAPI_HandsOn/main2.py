from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K.Rowling"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
    {"id": 4, "title": "Java", "author": "George Orwell"}
]

@app.get("/")
def home():
    return {"message": "Welcome to Book Management API"}


@app.get("/books")
def get_books():
    return {"books": books}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.get("/books/")
def get_books_by_author(author: str = None):
    if author:
        filtered_books = [book for book in books if book["author"] == author]
        return {"books": filtered_books}
    return {"books": books}
