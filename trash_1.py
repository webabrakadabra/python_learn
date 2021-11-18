class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, val):
        if isinstance(val, Point):
            x = ((self.x - val.x)**2 + (self.y - val.y)**2)**0.5
            return x
        else:
            print("Передана не точка")