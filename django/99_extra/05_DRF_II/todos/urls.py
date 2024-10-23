from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/<int:todo_pk>/', views.todo_detail),
    # recommend를 생성하기 위한 경로를 작성한다.
    # POST 요청이어야 할것이고, 참조할 todo의 pk값도 필요로 할 것이다.
    # 경로를 작성할땐, `todos와 관련된 / todo_pk 를 포함한 / recommend를 위한`
    path('todos/<int:todo_pk>/recommends/', views.recommend_create),
    # todos app의 recommends의 상세 조회
    path('todos/recommends/<int:recommend_pk>/', views.recommend_detail),
]
