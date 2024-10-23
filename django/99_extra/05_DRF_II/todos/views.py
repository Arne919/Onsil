from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Todo, Recommend
from .serializers import TodoSerializer, TodoListSerializer, RecommendSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'DELETE'])
def todo_detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# POST 요청만 허용 할 것이다.
@api_view(['POST'])
def recommend_create(request, todo_pk):
    # todo_pk를 받아온 이유 -> 그 todo를 조회하기 위해
    todo = Todo.objects.get(pk=todo_pk)
    # 게시글 생성과 완전히 동일한 코드를 적기만 하면 된다.
    if request.method == 'POST':
        # form = RecommendForm(request.POST)
        serializer = RecommendSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            '''
            # 잠깐 멈칫. -> todo 정보 db에 반영하기 전에 넣어줘야하는데?
            serializer.save(commit=False)
            serializer.todo = todo
            serializer.save()
            '''
            # For example: 'serializer.save(owner=request.user)'.'
            # save(keyword arguments)
            # 내가 DB에 commit하기전 넣어줘야할 field가 여러개 라고 하더라도
            # 그냥 전부 kwargs 형태로 한번에 다 집어넣으면 된다.
            serializer.save(todo=todo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def recommend_detail(request, recommend_pk):
    recommend = Recommend.objects.get(pk=recommend_pk)
    if request.method == 'GET':
        serializer = RecommendSerializer(recommend)
        return Response(serializer.data)
