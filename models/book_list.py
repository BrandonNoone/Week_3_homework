from models.book import Book  

book_1 = Book("A court of thorns and roses", "Sarah J. Maas", "Fantasy")
book_2 = Book("Gullivers travels", "Jonathan Swift","Satire")
book_3 = Book("A court of mist and fury", "Sarah J. Maas", "Fantasy")

books = [book_1,book_2,book_3]

def add_new_book(book):
    books.append(book)

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break
    books.remove(book_to_delete)