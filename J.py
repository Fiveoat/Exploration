class Complex:
    def __init__(self):
        self.real = 0
        self.imaginary = 0

    def prompt_for_values(self):
        self.real = input("Please enter the real part: ")
        self.imaginary = input("Please enter the imaginary part: ")
        print("")

    def display(self):
        print(f"{self.real} + {self.imaginary}i")

    def main(self):
        self.display()
        self.prompt_for_values()
        self.prompt_for_values()
        self.display()


def main():
    complex1 = Complex()
    complex2 = Complex()
    print("The values are:")
    complex1.display()
    complex2.display()
    print("")
    complex1.prompt_for_values()
    complex2.prompt_for_values()
    print("The values are:")
    complex1.display()
    complex2.display()

main()
