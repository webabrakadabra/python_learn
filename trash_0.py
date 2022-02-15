class Cat:
    count = 0
    def __init__(self, name='NoName', age=1):
        self.change_name(name)
        self.change_age(age)
        Cat.count = Cat.count + 1

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def print_count(self):
        print(Cat.count)