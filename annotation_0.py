"""
Анотації потрібні для підвищення інформативності кода.
За допомогою сторонніх плагінів типу mypy
можно аналізувати код та відловлювати помилки
"""


def calculate_price(unit_price: float, quantity: int) -> float:
    return unit_price * quantity


if __name__ == '__main__':
    print(calculate_price(5, 2))

