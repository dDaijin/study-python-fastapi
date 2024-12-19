class Animal:
    def __init__(self, name, sub, age, sound):
        self.name = name
        self.sub = sub
        self.age = age
        self.sound = sound
    def make_sound(self):
        print(f"{self.sound}..........  said {self.name}")

saying = Animal("Lion", "Cat", 5, "Roarhhhh")
saying2 = Animal("Wolf", "Dog", 3, "Baaark")
saying.make_sound()
saying2.make_sound()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        print(f"лоща дорівнює = {self.height * self.width}")
ploscha = Rectangle(7, 8)
ploscha2 = Rectangle(76, 12)
ploscha3 = Rectangle(8, 22)
ploscha.calculate_area()
ploscha2.calculate_area()
ploscha3.calculate_area()