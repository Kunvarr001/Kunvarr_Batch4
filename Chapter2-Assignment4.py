#Assignment 4: Converted C# Code to Python Following SRP

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page_index = 0

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def turn_page(self):
        if self.current_page_index < len(self.pages) - 1:
            self.current_page_index += 1

    def get_current_page(self):
        if self.pages:
            return self.pages[self.current_page_index]
        return None

class LibraryLocation:
    def __init__(self, shelf, room):
        self.shelf = shelf
        self.room = room

    def get_location(self):
        return f"Shelf {self.shelf}, Room {self.room}"

class BookSaver:
    def save_to_file(self, book):
        filename = f"{book.get_title()} - {book.get_author()}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            content = f"Title: {book.get_title()}\nAuthor: {book.get_author()}\n"
            content += "\n".join(book.pages)
            file.write(content)
        return filename

class Printer:
    def print_page(self, page):
        raise NotImplementedError("Subclasses should implement this!")

class PlainTextPrinter(Printer):
    def print_page(self, page):
        print(page)

class HtmlPrinter(Printer):
    def print_page(self, page):
        print(f'<div style="single-page">{page}</div>')


"""
The original C# Book class does not follow the Single Responsibility Principle (SRP) because it handles multiple responsibilities in a single class:
--Multiple Responsibilities in One Class:
    1. Book manages book content (getTitle, getAuthor, turnPage, getCurrentPage)
    2. It also handles library location and save function.
"""