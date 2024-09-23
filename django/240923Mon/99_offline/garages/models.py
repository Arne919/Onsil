from django.db import models

# Create your models here.
# 전세계 모든 파이썬 개발자는 class 이름을
# PascalCase로 작성한다.
class Garage(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_avaliable = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # name = models.TextField()

# g1 = Garage()
# g1.location = '값을 할당'