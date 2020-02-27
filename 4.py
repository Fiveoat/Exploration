
def fib(num):
    if num == 1:
        return 0
    elif num == 1:
        return 1
    elif num > 2:
        return fib(num - 1) + fib(num - 2)


print(fib(20))