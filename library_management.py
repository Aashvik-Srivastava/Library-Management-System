library = []


def add_books():
    book = input("enter book name:")
    library.append(book)
    print(f"{book} has been added")

    def issue_book():
     book = input("Enter book name you want to issue:")
    if book in library:
        library.remove(book)
        print(f"{book} has been issued ")
    else:
        print("book not found")

    



 