class Counter:
    def start_from(self, num=0):
        self.num = num

    def increment(self):
        self.num += 1

    def display(self):
        print(f"Текущее значение счетчика = {self.num}")

    def reset(self):
        self.num = 0