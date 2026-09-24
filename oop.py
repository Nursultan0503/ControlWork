from abc import ABC, abstractmethod
import math

# ==========================================
# 1. ИНКАПСУЛЯЦИЯ
# ==========================================
class Person:
    def __init__(self):
        # Инициализируем приватный атрибут (два нижних подчеркивания)
        self.__age = 0

    def set_age(self, age):
        if age < 0:
            print("Ошибка: Возраст не может быть отрицательным!")
        else:
            self.__age = age

    def get_age(self):
        return self.__age

print("--- 1. Инкапсуляция ---")
p = Person()
p.set_age(25)
print(p.get_age())  # Вывод: 25
p.set_age(-5)       # Должна быть ошибка или предупреждение


# ==========================================
# 2. НАСЛЕДОВАНИЕ
# ==========================================
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

print("\n--- 2. Наследование ---")
dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.name, dog.speak())  # Вывод: Buddy Woof
print(cat.name, cat.speak())  # Вывод: Kitty Meow


# ==========================================
# 3. ПОЛИМОРФИЗМ
# ==========================================
class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

# Общая функция, которая вызывает метод move() у переданного объекта
def move(vehicle):
    return vehicle.move()

print("\n--- 3. Полиморфизм ---")
car = Car()
bike = Bicycle()
print(move(car))   # Вывод: Car is driving
print(move(bike))  # Вывод: Bicycle is pedaling


# ==========================================
# 4. АБСТРАКЦИЯ
# ==========================================
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Формула площади круга: π * r^2
        return round(math.pi * (self.radius ** 2))

print("\n--- 4. Абстракция ---")
rect = Rectangle(10, 5)
circle = Circle(7)
# В ТЗ преподавателя опечатка (10*5 = 50, а не 55). Код выдаст правильные 50.
print(rect.area())    
print(circle.area())  # Вывод: 154