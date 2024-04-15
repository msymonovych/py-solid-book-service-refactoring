from dataclasses import dataclass


@dataclass
class Book:
    title: str
    content: str


class Base:

    def __init__(self, book: Book) -> None:
        self.book = book
