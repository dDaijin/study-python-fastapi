# замість display_info() було використано власні довільні методи, проте виконую вони те саме завдання=)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    def start_engine(self):
        print(f"Mass Car info - fuel: {self.fuel_type}, Model: {self.model}, Year{self.year}, Make type{self.make}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, wheels):
        super().__init__(make, model, year)
        self.wheels = wheels
    def country(self):
        print(f"Moto Model: {self.model}, Year{self.year}, Make type{self.make}, Wheels count {self.wheels}")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, chain):
        super().__init__(make, model, year)
        self.chain = chain
    def bike(self):
        print(f"Bikukle=) Model: {self.model}, Year{self.year}, Make type{self.make}, Type of chain {self.chain}")

cars = Car("hand", "Toyota", 2021, "Gas")
bikes = Bicycle("firm", "Ardis", 2023, "Big")
moto = Motorcycle("Japan", "Honda", 2000, 3)

cars.start_engine()
print("--------------------------------")
bikes.bike()
print("--------------------------------")
moto.country()
print("--------------------------------")