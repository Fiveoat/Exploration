from random import randint

MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """
    if len(items) > 1:
        mid_index = len(items) // 2
        left = items[:mid_index]
        right = items[mid_index:]
        merge_sort(left)
        merge_sort(right)
        x = 0
        y = 0
        z = 0
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                items[z] = left[x]
                x += 1
            else:
                items[z] = right[y]
                y += 1
            z += 1
        while x < len(left):
            items[z] = left[x]
            x += 1
            z += 1
        while y < len(right):
            items[z] = right[y]
            y += 1
            z += 1


def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests the merge sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    merge_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()


