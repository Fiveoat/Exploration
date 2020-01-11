def main():
    lines = 0
    words = 0
    file = input("Enter file: ")
    with open(file) as contents:
        for line in contents:
            word = line.split()
            lines += 1
            words += len(word)
    print(f"The file contains {lines} lines and {words} words.")


if __name__ == "__main__":
    main()
