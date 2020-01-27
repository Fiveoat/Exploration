
def get_user_input():
    while True:
        text = input("Input: ")
        try:
            text = int(text)
            print("Correct input!")
            break
        except ValueError:
            print("Not valid input. Try again.")
            continue

get_user_input()