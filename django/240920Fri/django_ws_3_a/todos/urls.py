from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index),
    path('create_todo/', views.create_todo),
    path('<work>/', views.detail),
]
