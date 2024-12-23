# Завдання 1
class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password
#отримати загальну інформацію
    def get_info(self):
        return self.__dict__
    
#отримати імя
    def get_name(self):
        return self._name
    
#отримати email
    def get_email(self):
        return self._email
    
#отримати password
    def get_password(self):
        return self._password

 # встановити загальну інформацію
    def set_info(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password

 # встановити імя користувача
    def set_name(self, name):
        self._name = name

 # встановити емейл
    def set_email(self, email):
        self._email = email

 # встановити пароль 
    def set_password(self, password):
         self._password = password




user = User("Igor", "igor@ukr.net", "Qwert123")
print(user.get_info())

user.set_info("Petro", "petro@gmail.com", "trewq321")
print(user.get_info())

user.set_name("Oleg")
print(user.get_info())

user.set_email("oLeg@gmail.com")
print(user.get_info())

user.set_password("password123")
print(user.get_info())


# Завдання 2
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def perimetr(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    def perimetr(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side
    def calculate_area(self):
        return self.first_side * self.second_side
    def perimetr(self):
        return 2*self.first_side + 2*self.second_side

class Triangle(Shape):
    def __init__(self, side, high):
        self.side = side
        self.high = high
    def calculate_area(self):
        return  0.5 * self.side * self.high
    def perimetr(self):
        return 3*self.side

def print_shape(shape):
    print(f"Area {shape.calculate_area()}")
    print(f"Perimeter {shape.perimetr()}")

circle = Circle(6)
rectangle = Rectangle(4, 5)
triangle = Triangle(4, 2)

print("Circle:")
print_shape(circle)
print("--------------------------")
print("Rectangle:")
print_shape(rectangle)
print("--------------------------")
print("Triangle:")
print_shape(triangle)
print("--------------------------")


# Завдання 3
# Для прикладу розглянемо мною написаний код. 
# інкапуляція використовується в даній частині коду
# class User:
    # def __init__(self, name, email, password):
    #     self._name = name
    #     self._email = email
    #     self._password = password
# дані заносяться в protected та в подальшому не викликаються на пряму, а лише через окремі класи
# які унаслідували дані атрибути

# Абстрактний клас вводиться в цьому коді

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     def calculate_area(self):
#         pass
#     def perimetr(self):
#         pass
# та використовується в подальшому вже повноцінно в кінці коду в функціях інших класів він може виконувати,
# різні обчислювані дії, проте завдяки абстрактному класу, простіше звернутись до нього та вивести всі необхіді дані
# аніж окреми до кожного класу писти вивідну функцію 




