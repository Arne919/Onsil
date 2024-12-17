from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def userinfo(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)