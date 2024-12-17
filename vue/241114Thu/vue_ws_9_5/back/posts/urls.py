from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.category_list),
    path('category/', views.category_create),
    path('posts/', views.post_list_create),
    path('posts/<int:post_pk>/', views.post_detail),
    path('posts/<int:post_pk>/comments/', views.comment_create),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/', views.comment_delete),
]