from django.db import models
from django.contrib.auth.models import AbstractUser

'''
class Article(models.Mdoel):
    # 내가 참조하는 대상 user
    # N의 입장에서 작성되는 변수명 -> 내가 참조하는 대상
        # `참조` 말이 어렵게 느껴진다면? 
        # 내가 붙들고 있는 대상. 내가 의존하고 있는 대상.
    user = models.ForeignKey(...)

'''

# Create your models here.
class User(AbstractUser):
    # 구독을 위한 MTMF 관계를 형성해 보자.
    # 1:N 관계에서, N의 입장에서 FK 필드를 정의할때 변수명은 어떤의므로?
    # 내가 구독하고 있는 저 사람
        # 나 (pk=1) : 내가 구독하는 저 사람 (pk=2)
        # models.ManyToManyField(to = "참조할 모델 명")
        # 굳이 settings에서 거쳐서 올 필요 없이 `나 자신` -> self
            # 왜 self 라고 하는 부분은 `문자열?`
            # self 변수를 정의 한 적은 없죠?
    subscription = models.ManyToManyField(
        # self -> attribute Error or NameError (그런 변수 정의한적 없으니까)
        'self',
        # 대칭구조는 서비스를 어떻게 만들었냐에 따라 서로 달라질 수 도 있다.
        # 구독 시스템도 마찬가지로, 내가 상대방을 구독한다고해서
        # 반드시 상대방도 나를 구독해야만 하는것은 아니다.
        symmetrical=False,
        # 자기 자신과 MTM 관계를 맺으면서 비대칭구조로 만들게 될떄는
        # 되도록이면, 무조건, 역참조명을(related_name) 만들어주는게 좋다.
            # 구독자
        # `self`로 다대다 관계를 맺을땐
        # 컬럼명이나, 역참조 매니저명이나 둘다 `나`를 기준으로 생각하는게 편하다.
        related_name='subscriber'
    )
    # MTMF 관계는 A 모델과 B 모델이 서로가 서로에게 영향을 미치는 것.
        # 내가 저 B라고 하는 객체를 붙잡고 있게 될떄,
        # 상대방도, 나를 붙잡게 되는게 기본 값이다.
    # 서비스 구축할때, 친구 관계 (친구 신청) -> 서로 친구 관계를 맺는것

    # self (A to A) 형식의 다대다 관계이긴 하지만, 대칭적 구조라면?
    # 이때는 왜 역참조 매니저명을 안만들어도 되느냐?
        # 내가 저 사람을 친구라고 생각한다.
            # request.user.friends
        # 저 사람이 나를 친구라고 생각한다.
            # person.friends
    # 물론 이렇게 만든다고 해서, 역참조 매니저가 없어지는건 아니다.
    # friends = models.ManyToManyField('self')

    
