#
#

# 그럼 프레임워크는 혹시 라이브러리를 모아놓은건가요
# 그건 아님

# 다른 '모듈'에 있는 클래스 가져오기
# 단, 명시성은 지켜주자
from .base import Person

# 학생 객체 -> 이름, 나이, 먹는다는 행위
# 상속

class Student(Person):    # 상속할 부모 클래스를 ()안에 작성한다.
    pass
    
s1 = Student('학생', 29)
print(s1.name)
s1.eat()