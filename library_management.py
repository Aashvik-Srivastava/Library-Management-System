library = []


def add_books():
    book = input("enter book name:")
    library.append(book)
    print(f"{book} has been added")

    add_books()



 