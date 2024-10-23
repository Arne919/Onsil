from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 여기에 정의해 두진 않았지만.. User는 분명.. Diary랑 관계를 맺고있음.
# 그럼.. User도 Diary에 대한 정보를 받아 올 수 있으면 좋겠는데?
# -> django가 제공해주는 기능이 바로 manager다...
    # 1:N을 배우기전까지 우리가 아는 manager는 objects 뿐이었다.
    # Model.objects.~~
# 1:N을 배우고 난 후에는 역참조 매니저
    # 나한테 (User class에) 정의된적 없는 상대방 (나를 참조하고있느 Diary)에
    # 대한 정보를 모아서 조회할 수 있도록 해주는 매니저가 있으면 좋겠다.
    # 그게 역참조 매니저고, 그 역참조 매니저는 어떻게 이름이 만들어지느냐?
    # 나를 참조하고있는 클래스명_set (소문자로)
# MTMF로 나를 참조하고 있는 Diary의 전체 목록을 보고 싶다면?
# 나는 나를 참조하는 클래스명_set (역참조 매니저)를 통해서 찾을수 있겠다.
    # user.diary_set.all()
class User(AbstractUser):
    pass
