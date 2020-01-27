class Person:
    def __init__(self):
        self.name = "anonymous"
        self.birth_year = "unknown"

    def display(self):
        print(self.name + f" (b. {self.birth_year})")


class Book:
    def __init__(self):
        self.title = "untitled"
        self.publisher = "unpublished"
        self.author = Person()

    def display(self):
        title = self.title
        publisher = self.publisher
        print(title)
        print("Publisher: ")
        print(publisher)
        print("Author: ")
        self.author.display()



def main():
    book = Book()
    book.display()
    print("")
    print("Please enter the following: ")
    book.author.name = input("Name: ")
    book.author.birth_year = input("Year: ")
    book.title = input("Title: ")
    book.publisher = input("Publisher: ")
    print("")
    book.display()


if __name__ == "__main__":
    main()


