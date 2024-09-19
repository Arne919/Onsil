from django.urls import path
from . import views


urlpatterns = [
    # main 경로로 요청이 들어오면, todos 앱 패키지 내에 있는
    # views.py 모듈 안에 있는 main 함수를 실행 시켜줘.
    path('main/', views.main),
    path('create/', views.create),
]