class Phone:
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        self.area_code = input("Area Code:")
        self.prefix = input("Prefix:")
        self.suffix = input("Suffix:")

    def display(self):
        print(f"Phone info:\n({self.area_code}){self.prefix}-{self.suffix}")

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.email = ""

    def prompt(self):
        self.email = input("Email:")

    def smart_display(self):
        print(f"Phone info:\n({self.area_code}){self.prefix}-{self.suffix}\n{self.email}")

def main():
    phone = Phone()
    print("Phone:")
    phone.prompt_number()
    print("")
    phone.display()
    print("")
    smart = SmartPhone()
    print("Smart phone:")
    smart.prompt_number()
    smart.prompt()
    print("")
    smart.smart_display()

if __name__ == '__main__':
    main()