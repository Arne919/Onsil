"""
URL configuration for todo_list_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # DRF로 API형태 사이트를 만들려고 한다면?
    # 왜 시작 경로를 항상 `api/v1/` 이라는 이름으로 만드는걸까?
    # 이렇게 만들어야만 API가 되는걸까?
        # 당연히 아니다.
    # 대체로 관례적으로, API 서버라면, 일반적인 웹서비스랑은 다르기떄문에
    # api라는 것을 명시해 주는 것이 좋다. 
        # 그리도 뒤에 v1은 그냥 버젼 1 이라는 뜻임.
    path('api/v1/', include('todos.urls'))
]
