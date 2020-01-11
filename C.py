def prompt_filename():
    # filename = input("Give")
    filename = "test.txt"
    print(f"Opening file {filename}")
    f = open(filename)
    return f


def parse_file(file):
    pride_count = 0
    pride = "pride"
    for line in file:
        words = line.split()
        print(words)
        if pride in words:
            pride_count += 1
    print(f"The word pride occurs {pride_count} times in this file.")


def main():
    file = prompt_filename()
    parse_file(file)


if __name__ == "__main__":
    main()
