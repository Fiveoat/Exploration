class GPA:
    def __init__(self):
        self.gpa = 0.0

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, letter):
        self.gpa = letter

    def get_letter(self):
        gpa = self.get_gpa()
        if .99 > gpa >= 0.0:
            return "F"
        elif 1.99 > gpa >= 1.0:
            return "D"
        elif 2.99 > gpa >= 2.0:
            return "C"
        elif 3.99 > gpa >= 3.0:
            return "B"
        elif gpa == 4.0:
            return "A"

    def set_letter(self, letter):
        if letter == "A":
            self.set_gpa(4.0)
        elif letter == "B":
            self.set_gpa(3.0)
        elif letter == "C":
            self.set_gpa(2.0)
        elif letter == "D":
            self.set_gpa(1.0)
        elif letter == "F":
            self.set_gpa(0.0)




def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))


if __name__ == "__main__":
    main()
