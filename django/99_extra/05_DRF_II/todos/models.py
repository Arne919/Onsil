from django.db import models

# Create your models here.
class Todo(models.Model):
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)

# DRF로 API를 구현해도, DB에 만들어질 table을 정의하는 방법이 달라지지는 않는다.
class Recommend(models.Model):
    # recommend는 참조할 todo가 필요하고,
    # DB에 그 참조할 todo가 없어지면, 같이 삭제하기로했다.
    # 그런데, loaddata 하려고 할떄,
    # recommend를 먼저 삽입하려고 하면,
    # 당연히 DB에 todo가 없으니. 삽입이 안된다.
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    content = models.TextField()

'''
    그렇다면 loaddata를 진행할떄,
    fixtures가 여러개라면 어떻게 해야하는가?
    매번 모델의 관계를 생각해서, 순서에 맞춰서 삽입해야 하는가.
    -> 개발자는 똑같은거 여러번하기 싫어한다.

    데이터 삽입할떄, 필요한거 한번에 다 때려넣자.
'''