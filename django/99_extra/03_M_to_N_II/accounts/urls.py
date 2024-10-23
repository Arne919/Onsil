from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # variable routing에 문자열을 받도록 하는 경로가 있다면
    # 그 아래에는, 문자열을 받도록 하는 경로와 조금 다르게 구변할 수 있는 추가 경로를 작성하거나
    # 혹은, 이렇게 문자열만 받는 경로는 항상 urlpatterns 리스트의 제일 마지막에 넣어주는게 좋다.
        # 얘는 말 그대로 모든 문자열을 다 변수 `username`에다가 집어넣는 친구다.
        # 즉, `login` 이 됐든, `logout`이 됐든, `1`이 됐든 전부다 `username`변수에 할당해버림.
        # 그럼....? 만약, `login`경로에 대한 처리를 profile 경로에 대한 처리보다 나중에 하게되면?
        # login 페이지로 갈 수 있는 방법이 없어진다.
        # 주소창에 입려된 login이 profile view 함수의 username 변수에 들어가버려서, 
        # 그 밑으로는 확인할 이유가 없기 떄문이다.
            # 왜냐? 리스트는 순차적으로 순회하기때문에.
    # 인스타그램 -> django로 만들어짐
    # 인스타그램 url 작동방식도 지금 설명하는거랑 똑같겠네?
    # 그래서 인스타그램 계정 생성시에 계정명을 유명한 외국 지명이나, 관공서 등으로는 못만들게 막혀있어요.
        # 혹은 `login` `logout` 과 같은 단어로도 사용하지 못하게 막혀있다.
    path('<username>/', views.profile, name='profile'),
    # 특정 주소로 요청이 들어오게 되면, 해당 주소의 담당자가, 적절한 일을 처리한다.
    # 누가 누구를 구독하느냐?
    # `누가` 라고하는 정보는 이미 `요청 보내는 사람`이라는 정보로 `request` 영역에 포함되어있다.
    # `누구를` 이라는 정보는 -> `누구를` 은 가입되어있는 유저가 많으면 많을수록 처리해야할 길이 많아진다.
    # variable routing
    path('<int:user_pk>/', views.subscribe, name='subscribe')
]