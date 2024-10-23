from django.urls import path
from . import views

# app_name 어디감? pattern_name 어디감?
    # API 서비스 구축할때는 쓸일이 없어서 안만들었다.
# 왜 쓸일이 없느냐?
    # 사용자가, 일반적인 문서를 조회 하는 요청이 아니라
    # DB에 변화를 주는 요청 (Create, Update, Delete)등을 보냈을떄,
    # 그 일에 대한 처리가 완료되고 난 후, 다른 조회페이지로
    # 사용자를 redirect 하기 위해서 이름을 썼었다.
    # 즉, view함수든, template이든 우리 서버가 우리 서버 내의
    # 다른 특정한 위치로 보낼때 쓰이기 떄문에 이름을 적어줬다.
# 근데 이제는?
    # 우리 서버가 하는 일은 오로지 JSON 데이터를 반환하는게 다다.
urlpatterns = [
    # 아래 두 경로는 완전히 다른 일을 한다.
    # GET http://127.0.0.1:8000/api/v1/
    # POST http://127.0.0.1:8000/api/v1/
    path('', views.todo_list_or_create),
    # URL을 작성할 떄는. method 역시도 이 식별자로써 사용된다는걸 기억해야한다.
    # POST 요청을 받는 'create' 경로 라고 적어둔 api가 있다면
        # `역전 앞`과 같은 말이다.
        # `앞 전`와 `앞` 자가 중복된0
    # path('create/', views.create),
]
