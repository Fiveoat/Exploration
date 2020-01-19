class RashDec:
    def __init__(self):
        self.numer = 0
        self.denom = 1

    def get_denom(self):
        self.denom = input("Enter the denominator: ")
        return self.denom

    def get_numer(self):
        self.numer = input("Enter the numerator: ")
        return self.numer

    def return_current_num_dom(self):
        print(f"{self.numer}/{self.denom}")


nums = RashDec()


def main():
    nums.return_current_num_dom()
    numerator = nums.get_numer()
    denominator = nums.get_denom()
    print(f"{numerator}/{denominator}")
    dec_form = float(numerator) / float(denominator)
    print(dec_form)


if __name__ == "__main__":
    main()
