from collections import deque

class Student:
    def __init__(self):
        self.name = ""
        self.course = ""

    def prompt(self):
        self.name = input("Enter name: ")
        self.course = input("Enter course: ")

    def display(self):
        print(f"Now helping {self.name} with {self.course}")


class HelpSystem:
    def __init__(self):
        self.waiting_list = deque()
        self.student = Student()

    def is_student_waiting(self):
        if len(self.waiting_list) > 0:
            return True

    def add_to_waiting_list(self):
        self.student.prompt()
        self.waiting_list.append(self.student)


    def help_next_student(self):
        if self.is_student_waiting():
            self.student = self.waiting_list.popleft()
            self.student.display()
        else:
            print("No one to help.")

def main():
    help_system = HelpSystem()
    while True:
        print("Options: ")
        print("1. Add a new student\n2. Help next student\n3. Quit")
        answer = input("Enter selection: ")
        if answer == "1":
            help_system.add_to_waiting_list()
            print("")
        elif answer == "2":
            help_system.help_next_student()
            print("")
        elif answer == "3":
            print("Goodbye")
            break
        else:
            print("Try again.")
            print("")

if __name__ == '__main__':
    main()