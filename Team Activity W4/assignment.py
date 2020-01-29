from date import Date


class Assignment:
    def __init__(self):
        self.name = "Untitled"
        self.start = Date()
        self.due = Date()
        self.end = Date()

    def assignment_prompt(self):
        self.name = input("Name: ")
        print("")
        print("Start Date: ")
        start = self.start.date_prompt()
        print("")
        print("Due Date: ")
        due = self.due.date_prompt()
        print("")
        print("End Date: ")
        end = self.end.date_prompt()
        print("")

    def assignment_display(self):
        print(f"Assignment: {self.name}")
        print(f"Start Date: \n{self.start.date_display()}")
        print(f"Due Date: \n{self.due.date_display()}")
        print(f"End Date: \n{self.end.date_display()}")


def main():
    assignment = Assignment()
    assignment.assignment_prompt()
    assignment.assignment_display()


if __name__ == '__main__':
    main()
