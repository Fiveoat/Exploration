def prompt_number():
    number = - 1
    while number < 0:
        number = int(input("Enter a positive number: "))
        print("")
        if number < 0:
            print("Invalid entry. The number must be positive.")
        else:
            return number


def compute_sum(num1, num2, num3):
    return num1 + num2 + num3


def main():
    num1 = prompt_number()
    num2 = prompt_number()
    num3 = prompt_number()
    sum = compute_sum(num1, num2, num3)
    print("The sum is: " + str(sum))

if __name__ == "__main__":
    main()
