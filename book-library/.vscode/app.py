from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    year : int
    author : str
    title : str
    def init(book,title, year, author):
        book.year = year
        book.title = title
        book.author =author
    
books = {}


@app.get("/books/")
async def getbooks():
    return books

@app.get("/books/{id}")
def getbook(id : int):

    return books[id]

@app.post("/books/")
async def addBook(book : Book):
    global counter 
    counter += 1
    newID = counter
    books[newID] = {"title: ": book.title, "year: ": book.year, "author: ": book.author, }
    allbooks.append(book)
    return{"Id: ": newID, "book info: ": books[newID]}

@app.put("/books/{id}")
async def put_details(id: int, book: Book):
    books[id]["title"] = book.title
    books[id]["author"] = book.author
    books[id]["year"] = book.year

