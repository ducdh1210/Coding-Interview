from pydantic import BaseModel, Field
from typing import TYPE_CHECKING, Optional, Dict, List

if TYPE_CHECKING:
    from typing import TYPE_CHECKING


class Book(BaseModel):
    title: Optional[str] = Field(None, frozen=True)
    author: Optional[str] = None
    isbn: Optional[str] = None
    total_copies: Optional[int] = None
    available_copies: Optional[int] = None

    @classmethod
    def create(cls, title: str, author: str, isbn: str, total_copies: int):
        return cls(
            title=title,
            author=author,
            isbn=isbn,
            total_copies=total_copies,
            available_copies=total_copies,
        )

    def add_copy(self, num_copy: int):
        self.total_copies += num_copy
        self.available_copies += num_copy


class User(BaseModel):
    user_id: int
    name: str
    borrow_books: List[str] = Field(
        default_factory=list
    )  # List of ISBNs, duplicates allowed


class Library:
    def __init__(self):
        self.books: Dict[str, Book] = {}  # isbn --> Book
        self.users: Dict[str, User] = {}  # user_id --> User

    def add_book(self, book: Book):
        self.books[book.isbn] = Book

    def add_user(self, user: User):
        self.users[user.user_id] = User

    def borrow_book(self, user: User, book: Book):
        if book.available_copies <= 0:
            raise RuntimeError(f"No copies of {book.title} are available")

        user.borrow_books.append(book.isbn)
        book.available_copies -= 1

        print(f"user {user.user_id} {user.name} borrowed {book.title}")

    def return_book(self, user: User, book: Book):
        if book.isbn not in user.borrow_books:
            print(f"User {user.id} has not borrowed this book {book.title}")
            return

        user.borrow_books.remove(book.isbn)
        book.available_copies += 1
        print(f"{user.name} returned '{book.title}'")


library = Library()

book = Book.create(title="1984", author="George Orwell", isbn="123", total_copies=3)
user = User(user_id=1, name="Alice")

library.add_book(book)
library.add_user(user)

print(library)

library.borrow_book(user, book)
print(user.borrow_books)

print(book)

library.return_book(user, book)
print(book)
