def prompt_filename():
    filename = input("Input a file: ")
    print(f"Opening file {filename}")
    f = open(filename)
    return f


def parse_file(file):
    given_count = 0
    given_word = input("Enter a word to check for number of times in given file: ")
    for line in file:
        words = line.split()
        if given_word in words:
            given_count += 1
    print(f"The word {given_word} occurs {given_count} times in this file.")


def main():
    file = prompt_filename()
    parse_file(file)


if __name__ == "__main__":
    main()
