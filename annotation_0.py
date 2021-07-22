def calculate_price(unit_price: float, quantity: int) -> float:
    return unit_price * quantity


if __name__ == '__main__':
    print(calculate_price(5, 2))
