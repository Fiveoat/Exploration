class NegativeNumberError(BaseException):
    def __init__(self, message):
        super().__init__(message)


def get_inverse(n):
    n = float(n)

    if n < 0:
        raise NegativeNumberError("Error: The value cannot be negative.")

    return 1 / n


def main():
    n = input("Enter a number: ")
    try:
        result = get_inverse(n)
        print(f"The result is: {result}")
    except ValueError:
        print("Error: The value must be a number")
    except NegativeNumberError as e:
        print(e)
    except ZeroDivisionError:
        print(" Error: Cannot divide by zero")


if __name__ == "__main__":
    main()