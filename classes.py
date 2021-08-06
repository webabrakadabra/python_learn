"""Клас з конструктором."""


class Dog:
    """class Dog"""
    def __init__(self, age, name): # __init__ - конструктор класа, метод визиваєтья при створенні екз. класа
        self.age = age
        self.name = name
        print(age, name)


""" наслідування класу, метод __init__() класа потомка"""


class Car:
    """ проста модель автомобіля"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def odometer_update(self, miliage):
        if miliage >= self.odometer_reading:
            self.odometer_reading = miliage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -kWh battery")

my_tesla = ElectricCar('tesla', 'model s', 2011)
print(my_tesla.get_description_name())
my_tesla.describe_battery()
