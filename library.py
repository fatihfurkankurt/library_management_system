class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
    
    def __del__(self):
        self.file.close()
    
    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")
    
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter first release year: ")
        pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        self.file.flush()  # Verilerin dosyaya yazıldığından emin oluyoruz
    
    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for i, line in enumerate(lines):
            if line.startswith(title_to_remove):
                del lines[i]
                break

        self.file.seek(0)
        self.file.truncate()
        for line in lines:
            self.file.write(f"{line}\n")
        self.file.flush()

# "Library" sınıfı ile "lib" adında bir nesne oluşturduk
lib = Library()

# Menü etkileşimi
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")