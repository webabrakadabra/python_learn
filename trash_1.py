class Mono:
    attr = {
        "name": "Tom",
        "age": 12
    }

    def __init__(self):
        self.__dict__ = Mono.attr
