from django.db import models
# django가 가지고 있는 것중에 설정(configure)에 있는 settings
from django.conf import settings


# Create your models here.
# diary와 User의 M:N 관계를 정의한다.
    # 그럼 M:N 서로가 서로를 참조하고 있을때는? 누구한테 MTMF를 정의해야할까?
    # 그건 딱히 정해지진 않았다. 
# 1:N 관계를 정의할떄는 어디에 ForeignKey 설정해야 할까?
    # N의 입장에 외래키 설정을 진행했다.
    # N은 항상 반드시 참조하고 있는 대상 1이 누군지 알아야 하기 때문에

class Diary(models.Model):
    # 컬럼명 = 데이터타입(제약조건)
    # 컬럼명(변수명) : 여기에 어떤 데이터가 담길지 잘 나타낼 수 있는 이름
    # 다대다 관계도 `누구랑` 관계를 맺을 것이냐가 중요하므로, 상대방을 작성할
    # to= 라고 하는 인자를 받는다.
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        # User를 여기에 작성해야하는데...
        # User는 조금... 특별한 모델이다.
        # 1. 다른 app에 있는 모델이다.
        # 2. django가 기본적으로 제공하는 모델을 바꿔서 쓰는중이다.
        # 3. 그래서, 혼동을 막고자 항상 settings에 적어둔 AUTH_USER_MODEL
            # import를 받아와서 사용한다.
        settings.AUTH_USER_MODEL,
        # 실습 대로라면, user입장에서 다대다 관계를 맺고있는 diary를 찾기위해서
        # 역참조 매니저명을 diary_set이라고 써도 아무런 문제가 되지 않는다.
            # 근데, 만약에, user가 diary랑 다른관계를 이미 맺고 있었다면?
            # 1:N, M:N 규칙이 똑같기 떄문에,
            # 이미 User랑 Diary랑 1:N을 맺고 있는 상태였다면?
            # User가 본인을 참조하고 있는 Diary 정보를 얻을 수 있는 역참조 매니저
            # diary_set이 누구를 가리켜야할지 알 수가 없게된다.
        # related_name='like_diaries'
    )
    # MTMF를 사용해서 Diary와 User의 관계를 정의하는데,
    # 정의하는 방법이 1:N 할때와 똑같은데, 그냥 Field만 FK냐 MTMF냐만 다르다.
    # 사용하는 방법조차도 똑같다.
    content = models.CharField(max_length=125)
    picture = models.ImageField(blank=True, upload_to='diary/%y/%b/%a')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)