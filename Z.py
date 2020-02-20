class Shape:
    def __init__(self):
        super().__init__()
        self.name = ""

    def get_area(self):
        self.area = 1

    def display(self):
        print("{} - {:.2f}".format(self.name, self.get_area()))


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Circle"
        self.radius = 0.0

    def get_area(self):
        self.area = self.radius * 3.14


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Rectangle"
        self.length = 0.0
        self.width = 0.0

    def get_area(self):
        self.area = self.length * self.width
