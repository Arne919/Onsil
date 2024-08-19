# ws_7_a
my_lsit = [1, 2, 3]
my_dict = {'A': 1, 'B': 2, 'C': 3}
# print(dir(my_lsit))
# print()
# print(dir(my_dict))
# help(my_lsit)
# help(my_dict)


# ws_7_b
class Myth:
    type_of_myth = 0
    def __init__(self, name):
        self.name = name
        Myth.type_of_myth += 1
        print(self.name)
    @staticmethod
    def description():
        return f'신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.'
myth1 = Myth('dangun')
myth2 = Myth('greek & rome')
print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')
print(Myth.description())


# ws_7_c
class Car:
    wheels = 4
    def __init__(self, engine, driving_system, sound):
        self.engine = engine
        self.driving_system = driving_system
        self.sound = sound
    def drive(self):
        print(self.sound)
    def introduce(self):
        print(f'제 차의 엔진은 {self.engine} 방식이고, {self.driving_system} (으)로 동작합니다.')
    @classmethod
    def increase_wheels(cls):
        cls.wheels += 1
        print(f'법이 개정되어 모든 자동차의 필요 바퀴 수가 1증가하였습니다.')
    @staticmethod
    def description():
        return f'자동차(自動車, 영어: car, automobile)는 엔진에서 만든 동력을 바퀴에 전달하여 지상에서 승객이나 화물을 운반하는 교통 수단이다.'
car1 = Car('gasoline', '후륜구동', '부릉부릉')
car2 = Car('diesel', '전륜구동', '달달달달')
car3 = Car('hybrid', '4wd', '슈웅')

car1.drive()
car2.drive()
print(car2.engine)
print('===')
car1.introduce()
car3.introduce()
print('===')
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
Car.increase_wheels()
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
print(Car.description())


# ws_7_1
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
shape1 = Shape(5, 3)
print(shape1.width, shape1.height)


# ws_7_2
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)


# ws_7_3
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_perimeter(self):
        return (self.width + self.height) * 2
shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
shape1.calculate_perimeter()


# ws_7_4
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return (self.width + self.height) * 2
    def print_info(self):
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {area}')
        print(f'Perimeter: {perimeter}')
shape1 = Shape(5, 3)
shape1.print_info()


# ws_7_5
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'
shape1 = Shape(5, 3)
print(shape1)


# hw_7_2
class StringRepeater:
    def repeat_string(self, times, string):
        for _ in range(times):
            print(string)
repeater1 = StringRepeater()
repeater1.repeat_string(3, 'Hello')


# hw_7_4
class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 저는 {self.age}살 입니다.')
    @classmethod
    def number_of_people(cls):
        return cls.count
person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people())