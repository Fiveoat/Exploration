from csv import reader

# reader allows us to read the csv file
filename = input("Please enter the data file: ")


# this takes the input for the file that will be used in the functions


def calc_lowest_rate():
    data = []
    com_rates = []
    with open(filename) as file:
        csv_reader = reader(file)
        next(csv_reader)
        for items in csv_reader:
            data.append(items)
            com_rate = items[6]
            com_rates.append(com_rate)
        minimum = min(com_rates)
        for values in data:
            if values[6] == minimum:
                print("The lowest rate is:")
                print(values[2], f"({values[0]}, {values[3]}) -", f"${float(minimum)}")
                break


# this function calculates the lowest rate and prints out the data associated with it

def calc_highest_rate():
    com_rates = []
    data = []
    with open(filename) as file:
        csv_reader = reader(file)
        next(csv_reader)
        for items in csv_reader:
            data.append(items)
            com_rate = items[6]
            com_rates.append(float(com_rate))
        maximum = max(com_rates)
        for values in data:
            for x in values:
                if x == str(maximum):
                    print("The highest rate is:")
                    print(values[2], f"({values[0]}, {values[3]}) -", f"${float(maximum)}")
                    break


# this function calculates the highest rate and prints out the data associated with it

def calculate_ave_com_rate():
    total = 0
    items = 0
    with open(filename) as file:
        csv_reader = reader(file)
        next(csv_reader)
        for item in csv_reader:
            com_rate = item[6]
            items += 1
            total += float(com_rate)
    print(f"The average commercial rate is: {(total / items)}")


# this function calculates the average rate and prints out the data associated with it

def main():
    global filename
    print("")
    calculate_ave_com_rate()
    print("")
    calc_highest_rate()
    print("")
    calc_lowest_rate()


# this function runs all the functions and displays their results

if __name__ == "__main__":
    main()
