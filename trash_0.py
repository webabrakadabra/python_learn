def summa(*args: float) -> float:
    s = 0
    for el in args:
        s = el + s
    return s


print(summa(1, 2.2))
