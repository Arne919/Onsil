# conf 패키지에 있는 2개의 클래스 모두 가져오기
# from conf import students, teacher
from conf.students import Student
from conf.teacher import Teacher

s1 = Student('학생', 29)
t1 = Teacher('선생', 30)

t1.teach()