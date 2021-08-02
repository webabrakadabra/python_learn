"""Клас з конструктором."""


class Dog:
    """class Dog"""
    def __init__(self, age, name): # __init__ - конструктор класа, метод визиваєтья при створенні екз. класа
        self.age = age
        self.name = name
        print(age, name)

