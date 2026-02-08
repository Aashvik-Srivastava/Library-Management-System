library = []

def issue_book():
    book = input("Enter book name you want to issue: ")
    if book in library:
        library.remove(book)
        print(f"{book} has been issued")
    else:
        print("Book not found")

def return_book():
    book = input("Enter book name you want to return: ")
    library.append(book)
    print(f"{book} has been returned")

def view_book():
    if not library:
        print("No books are present in the library")
    else:
        print("List of books:")
        for idx, book in enumerate(library, start=1):
            print(f"{idx}. {book}")
    print()
