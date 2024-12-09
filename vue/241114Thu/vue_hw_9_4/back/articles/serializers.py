from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article

User = get_user_model()

class UserSerialier(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', )

class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerialier(read_only=True)

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content')

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerialier(read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'