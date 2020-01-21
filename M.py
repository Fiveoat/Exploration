odd = []
even = []
while True:
    num = int(input("Enter a number (0 to quit): "))
    if num == 0:
        print("")
        print("Even numbers:")
        for y in even:
            print(y)
        print("")
        print("Odd numbers:")
        for x in odd:
            print(x)
        break
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
