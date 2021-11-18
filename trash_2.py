class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{brand} {model}"

laptop1 = Laptop('samsung', 'x2', 12)
laptop2 = Laptop('samsungs', 'x332', 12)
