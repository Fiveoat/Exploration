def mult_by_2():
    while True:
        x = input("Enter a number: ")
        try:
            y = int(x) * 2
            print(f"The result is: {y}")
            break
        except Exception:
            print("The value entered is not valid")


if __name__ == '__main__':
    mult_by_2()