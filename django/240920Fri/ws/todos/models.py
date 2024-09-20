from django.db import models

# Create your models here.
# 할 일 목록을 위한 모델을 정의
class Todo(models.Model):
    # 할 일을 `어떤 데이터 타입으로` 저장 할 건지 정의
    work = models.CharField(max_length=100)
    # work = models.TextField()
    # 완료 여부를 저장
        # boolean -> check box -> True / False
        # 완료 했거나 / 안 했거나
    is_completed = models.BooleanField(default=False)
    # 언제 만들었는지를 저장
        # 날짜만 저장
            # models.DateField()
        # 시간만 저장
            # models.TimeField()
        # 날짜 + 시간 저장
            # models.DateTimeField()
    # 근데.. 날짜랑 시간이랑 같이 저장되게는 하고 싶기는한데..
    # 이걸... 내가 매번 todo 생성할때마다 오늘 날짜랑 시간을
    # 직접 적어줘야 하면 좀... 불편할지도?
    # 생성된 시점 시간은... python이 알아서 할 수 있지않나?
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.work