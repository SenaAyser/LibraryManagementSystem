class Library:

    def __init__(self, filename, mode='a+'):
        self.filename = filename
        self.mode = mode
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            raise

    def __del__(self):
        self.file.close()
    def list_books(self):
        self.file.seek(0)  # Move cursor to the beginning of the file (Bu kismi internetten arastirdim)
        books = self.file.read().splitlines()
        if not books:
            print("There is no book.")
        else:
            for book in books:
                print(book)

    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        book_release_date = input("Enter release year: ")
        book_num_pages = input("Enter number of pages: ")
        book_info = f"{book_title}, {book_author}, {book_release_date}, {book_num_pages}"
        self.file.write('\n'+book_info )

    def remove_book(self):
        book_name_to_remove = input("Please enter a book name to remove from book list: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        book_check = False
        for book in books:
            book_info  = book.split(",")
            if book_info[0] == book_name_to_remove:
                index_of_book = books.index(book)
                del books[index_of_book]
                book_check = True

        if not book_check:
            print("Please enter a valid book name to delete")
        else:
                self.file.truncate(0)

        for book in books:
            book_info = book.split(",")
            book_info_str = f"{book_info[0]}, {book_info[1]}, {book_info[2]}, {book_info[3]}"
            self.file.write(book_info_str + '\n')





while True:
    lib = Library('books.txt')
    print("*** MENU***\n1) List Books\n2) Add Book\n3) Remove Book")
    answer = input("Please make a choce: ")
    if answer == "q":
        break
    elif answer == "1":
        lib.list_books()
    elif answer == "2":
        lib.add_book()
    elif answer == "3":
        lib.remove_book()
    else:
        print("Please enter a valid number!")
