class User:
    active_user = 0 # class attribute

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_user += 1

    def logout(self):
        print(f"{self.first} has logged out")
        User.active_user -= 1

    def full_name(self):
        print(self.first, self.last)

    def initials(self):
        print(self.first[0], self.last[0])

    def likes(self, thing):
        print(self.first, "likes", thing)

    def is_senior(self):
        print(self.age >= 65)

    def birthday(self):
        self.age += 1
        print(f"Happy {self.age}th {self.first}")

    def say_hi(self):
        print("hi")


user1 = User("Joe", "Flack", 25)
user2 = User("Blanca", "Black", 23)

print(user1.first, user1.last)
print(user2.last, user2.age)
user2.full_name()
user1.full_name()
user2.initials()
user1.likes("Ice Cream")
user2.likes("Tacos")
# instance.attribute : ex. user1.first
user2.is_senior()
user2.birthday()
print(User.active_user)
user1.logout()
print(User.active_user)
# _name secret
# __name
# __name__ magic
