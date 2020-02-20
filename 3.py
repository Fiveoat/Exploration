from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def paycheck(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.hourly_wage = 0

    def display(self):
        print(f"{self.name} makes ${self.hourly_wage} per hour.")

    def paycheck(self):
        print(f"Paycheck amount is ${self.hourly_wage * 80} every two weeks.")


class SalaryEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.salary = 0

    def display(self):
        print(f"{self.name} makes ${self.salary} per year.")

    def paycheck(self):
        print(f"Paycheck amount is ${round(self.salary / 52 / 2)} every two weeks.")


def display_employee_data(employee):
    employee.display()
    employee.paycheck()


def main():
    employees = []
    command = ""
    while command != "q":
        command = input("Enter h, q, s: ")
        if command == "h":
            hourly = HourlyEmployee()
            hourly.name = "John"
            hourly.hourly_wage = 8
            employees.append(hourly)
        elif command == "s":
            salary = SalaryEmployee()
            salary.name = "Mike"
            salary.salary = 50000
            employees.append(salary)
        elif command == "q":
            break
    for employee in employees:
        employee.display()


if __name__ == '__main__':
    hourboi = HourlyEmployee()
    salboi = SalaryEmployee()
    salboi.name = "Hal"
    salboi.salary = 500000000
    hourboi.name = "Chesse"
    hourboi.hourly_wage = 12
    display_employee_data(hourboi)
    display_employee_data(salboi)
