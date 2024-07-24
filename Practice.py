class Car:
    def __init__(self):
        self.brand = "1992"
        self.model = "Corolla"
    def car(self):
        return f"Brand: {self.brand} and Model: {self.model}"

O1 = Car()
print(O1.car())