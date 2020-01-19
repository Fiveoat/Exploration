class Robot:
    fuel_to_perform = 0

    def __init__(self):
        self.fuel = 100
        self.xcoor = 10
        self.ycoor = 10
    # moves up
    def move_up(self):
        self.ycoor -= 1
        self.fuel -= 5

    # moves down
    def move_down(self):
        self.ycoor += 1
        self.fuel -= 5

    # moves left
    def move_left(self):
        self.xcoor -= 1
        self.fuel -= 5

    # moves right
    def move_right(self):
        self.xcoor += 1
        self.fuel -= 5

    # fires the laser
    def fire_laser(self):
        print("Pew! Pew!")
        self.fuel -= 15

    # displays fuel level
    def display_fuel(self):
        return self.fuel

    # displays the coordinates
    def display_position(self):
        print(self.xcoor, self.ycoor)

    # displays the coordinates and the fuel remaining
    def display_status(self):
        print(f"({self.xcoor}, {self.ycoor}) - Fuel: {self.fuel}")

    # makes sure that there is enough fuel for the task
    def fuel_to_perform_check(self):
        return Robot.fuel_to_perform <= int(self.display_fuel())

    # takes command and preforms according task
    def use_command(self):
        quit_value = 0
        insufficient = "Insufficient fuel to perform action"
        while quit_value == 0:
            command = input("Enter command: ")
            if command == "status":
                self.display_status()
            elif command == "right":
                Robot.fuel_to_perform = 5
                if self.fuel_to_perform_check():
                    self.move_right()
                else:
                    print(insufficient)
            elif command == "left":
                Robot.fuel_to_perform = 5
                if self.fuel_to_perform_check():
                    self.move_left()
                else:
                    print(insufficient)
            elif command == "down":
                Robot.fuel_to_perform = 5
                if self.fuel_to_perform_check():
                    self.move_down()
                else:
                    print(insufficient)
            elif command == "up":
                Robot.fuel_to_perform = 5
                if self.fuel_to_perform_check():
                    self.move_up()
                else:
                    print(insufficient)
            elif command == "fire":
                Robot.fuel_to_perform = 15
                if self.fuel_to_perform_check():
                    self.fire_laser()
                else:
                    print(insufficient)
            elif command == "quit":
                print("Goodbye.")
                quit_value += 1
                break


robot = Robot()

def main():
    while True:
        robot.use_command()
        break


if __name__ == "__main__":
    main()
