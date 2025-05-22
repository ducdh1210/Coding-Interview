from pydantic import BaseModel


class Book(BaseModel):
    title: str
    available: bool = False


book = Book(title="1984")
print(book.available)

book.available = True
print(book.available)


class Book(BaseModel):
    title: str
    available: bool = False

    class Config:
        frozen = True


book = Book(title="1984")
print(book.available)

book.available = False
print(book.available)
