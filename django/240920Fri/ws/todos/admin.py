from django.contrib import admin
# 현재 폴더와 같은 위치에 있는 models에 정의한 Todo class
from .models import Todo

# Register your models here.

# 관리자.사이트.등록(할 일)
admin.site.register(Todo)