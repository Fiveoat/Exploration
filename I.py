class Student:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.id = 0


def prompt_student():
    Student.first_name = input("Please enter your first name: ")
    Student.last_name = input("Please enter your last name: ")
    Student.id = input("Please enter your id number: ")
    return Student


def display_student(Student):
    user = Student
    print("Your information: ")
    print(f"{user.id} - {user.first_name}{user.last_name}")


def main():
    user = prompt_student()
    print("")
    display_student(user)


if __name__ == "__main__":
    main()
