class Person:
    # class variable 만든다.
    population = 0

    # 생성자 함수
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 인스턴스 생성 될때마다 population +1
        Person.increase()

    # 인스턴스 메서드
    def eat(self):
        print('밥을 먹는다.')
# 인스턴스
p1 = Person('사람', 10)
p2 = Person('인간', 30)
print(p1)   # Person class의 인스턴스 p1이다.
p1.eat()    # 인스턴스가 호출 할 수 있는 메서드
p2.eat()    # 모든 Person class의 인스턴스는 eat 메서드 호출 가능
