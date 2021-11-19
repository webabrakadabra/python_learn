class Zebra:
    count = 0

    def which_stripe(self):
        if self.count % 2 == 0:
            print("Полоска белая")
        else:
            print("Полоска черная")
        self.count += 1

