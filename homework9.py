# Завдання 1
# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def info(self):
#         return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}"
#     def __str__(self):
#         return self.info()
    
# class Update:
#     @staticmethod
#     def update_user(user, name = None, surname = None, age = None):
#         if name is not None:
#             user.name = name    
#         if surname is not None:
#             user.surname = surname
#         if age is not None:
#             user.age = age
#     @staticmethod
#     def delete(user):
#         user.name = None
#         user.surname = None
#         user.age = None

# infa = User("Oleg", "Shweps", 188)
# print(infa)

# Update.update_user(infa, surname="Jumaisinba")
# print(infa)

# Завдання 2


# from abc import ABC, abstractmethod

# class Shape:
#     @abstractmethod
#     def get_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
    
# class Recktangle(Shape):
#     def __init__(self, one_side, two_side):
#         self.one_side = one_side
#         self.two_side = two_side

#     def get_area(self):
#         return self.one_side * self.two_side
    
# class Culculator:
#     @staticmethod
#     def calculate(shape):
#         return shape.get_area()
    

# circle = Circle(5)
# rectangle = Recktangle(4, 6)

# print(f"Площа кола: {Culculator.calculate(circle)}")
# print(f"Площа прямокутника: {Culculator.calculate(rectangle)}")

# Завдання 3


# class Figure():
#     def perimets(self):
#         pass

# class Squere(Figure):
#     def __init__(self, side):
#         self.side = side
#     def perimets(self):
#         return self.side*4
    
# class Triangle(Figure):
#     def __init__(self, side):
#         self.side = side
#     def perimets(self):
#         return self.side * 3
    

# class Result():
#     @staticmethod
#     def calculate(figure):
#         return figure.perimets()

# squere = Squere(4)
# triangle = Triangle(3)


# print(f"Squere {Result.calculate(squere)}")
# print(f"Triangle {Result.calculate(triangle)}")

# Завдання 4

# class NetworkPrinter:
#     def __init__(self, connection):
#         self.connection = connection

# class Scanner(NetworkPrinter):
#      def __init__(self, connection, text_number):
#           super().__init__(connection)
#           self.text_number = text_number

        

# class Printer(Scanner):
#     def result(self):
#             if self.connection == True:
#                 print("---Welcome---")
#                 return self.count()
#             else :
#                 print("_--Error--_")
#                 return None
            
#     def count(self):
#          if len(self.text_number) >=20:
#               return f"Your text {self.text_number}"
#          else:
#               return "Not enough letters("
         

# text = Printer(connection=True, text_number="Принцип ISP стверджує, що клієнти не повинні залежати")
# resultat = text.result()
# print(resultat)

# Завдання 5

# Done










