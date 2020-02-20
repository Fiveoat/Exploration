class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = input("Publication Year: ")

    def display_book_info(self):
        print(f"{self.title} ({self.publication_year}) by {self.author}")


class TextBook(Book):
    def __init__(self):
        super().__init__()
        self.subject = ""

    def prompt_subject(self):
        self.subject = input("Subject: ")

    def display_subject(self):
        print(f"Subject: {self.subject}")


class PictureBook(Book):
    def __init__(self):
        super().__init__()
        self.illustrator = ""

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print(f"Illustrated by {self.illustrator}")


def main():
    book = Book()
    book.prompt_book_info()
    print("")
    book.display_book_info()
    print("")
    tbook = TextBook()
    tbook.prompt_book_info()
    tbook.prompt_subject()
    print("")
    tbook.display_book_info()
    tbook.display_subject()
    print("")
    pbook = PictureBook()
    pbook.prompt_book_info()
    pbook.prompt_illustrator()
    print("")
    pbook.display_book_info()
    pbook.display_illustrator()


if __name__ == '__main__':
    main()
