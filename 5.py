

class Pet:
    allowed = ['cat', 'dog', 'fish']
    def __init__(self, name, sp):
        if sp not in Pet.allowed:
            raise ValueError(f"You can't have a {sp} pet!")
        self.name = name
        self.sp = sp
    def set_sp(self, sp):
        pass


cat = Pet("Blue", "cat")
tiger = Pet("Tony", "Tiger")

#
# class Cat(Pet):
#     def __init__(self):
#
