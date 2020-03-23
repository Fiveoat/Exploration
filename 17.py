def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    """Easiest Way"""
    # numbers.sort()
    """Bubble Sort"""
    # for x in range(0, len(numbers) - 1):
    #     for y in range(0, len(numbers) - 1 - x):
    #         if numbers[y] > numbers[y + 1]:
    #             numbers[y], numbers[y + 1] = numbers[y + 1], numbers[y]
    """Selection Sort"""
    # for x in range(0, len(numbers) - 1):
    #     min_index = x
    #     for y in range(x + 1, len(numbers)):
    #         if numbers[y] < numbers[min_index]:
    #             min_index = y
    #     if min_index != x:
    #         numbers[x], numbers[min_index] = numbers[min_index], numbers[x]
    """Insertion Sort"""
    for x in range(1, len(numbers)):
        y = x - 1
        while numbers[y] > numbers[y + 1] and y >= 0:
            numbers[y], numbers[y + 1] = numbers[y + 1], numbers[y]
            y -= 1


def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers


def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)


def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)


if __name__ == "__main__":
    main()
