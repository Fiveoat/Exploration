class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def prompt_for_point(self):
        self.x = input("Enter x: ")
        self.y = input("Enter y: ")


class Circle(Point):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def prompt_for_circle(self):
        self.prompt_for_point()
        self.radius = input("Enter radius: ")

    def display(self):
        print("Center: ")
        print(f"({self.x},{self.y})")
        print(f"Radius: {self.radius}")


circle = Circle()
circle.prompt_for_circle()
circle.display()
