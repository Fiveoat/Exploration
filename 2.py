from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self.name = ""

    def display(self):
        print("{} - {:.2f}".format(self.name, self.get_area()))

    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Circle"
        self.radius = 0.0
        self.area = 0.0

    def get_area(self):
        self.area = 3.14 * self.radius * self.radius
        return self.area


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Rectangle"
        self.length = 0.0
        self.width = 0.0
        self.area = 0.0

    def get_area(self):
        self.area = self.length * self.width
        return self.area


def main():
    shapes = []
    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            circle = Circle()
            circle.radius = radius
            shapes.append(circle)

        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            rectangle = Rectangle()
            rectangle.length = length
            rectangle.width = width
            shapes.append(rectangle)

    for shape in shapes:
        shape.display()


if __name__ == "__main__":
    main()
