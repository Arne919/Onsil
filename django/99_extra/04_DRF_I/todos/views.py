# rest_framework의 힘을 빌려서 JSON 데이터를 반환(response)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
# 이제는 django의 일반적인 view함수가 아니라
# rest framework가 특별히 (api에 맞도록) view함수를 `꾸며줄거다.`
# api view함수로 만들려고 한다면, 지키면 좋은것이 있다.
    # 이 view함수는 어떤 메서드`들`을 허용할 것이냐를 적어주자.
    # 메서드`들` -> python에서 다수의 데이터를 담을 수 있는 방법? list
@api_view(['GET', 'POST'])
def todo_list_or_create(request):
    # 이제 이 view 함수는 GET이거나 POST일떄 서로 다른 일을 해야한다.
    # 그러면? if문으로 조건 분기 해야한다.
    if request.method == 'GET':
        # 전체 todo를 조회한다.
        todos = Todo.objects.all()
        '''
        # 아래 방식으로도 가능은 하지만, 기능을 다 만들어 줬기 떄문에... 그걸쓰는게 더 편하다.
        data = []
        for todo in todos:
            temp = {
                'work': todo.work,
                'content': todo.content,
                'is_completed': todo.is_completed,
                'created_at': todo.created_at
            }
            data.append(temp)

        # 열심히 모아둔 todo들을 사용자에게 어떻게 넘기냐?
        # 이제부터는 JSON 형태로 넘길거다. 그건 어떻게 하는 건데?
            # rest_framework의 힘을 빌려서 반환한다.
        # TypeError   : Response가 JSON 형태로 바꿀수 없는 데이터를 넘겼다.
            # JSON으로 변환 가능한 데이터를 넣어보자.
            # return Response({'test': 'test'})
        return Response(data)
        '''
        # DRF는 serilalizer를 만들어줬다.
        # 이전에 django의 forms가 하던일을 serializer가 완전히 대체해준다.
            # 거기에 더해서 몇가지 기능이 추가가 됐다.
        # TodoSerializer에게 내가 가지고 있는 todos 정보를
        # 너가 가지고 있는 필드들에 맞게 JSON형태로 바꿔줘. 그리고 변수에 담아줘
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # POST 요청이 왔을떄? 우리가 해야 하는 일은?
        # 이전에 django에서 하던일을 그대로 하면됨.
        # 대신에 forms가 하던일을 이제는 serialziers가 대신함.
            # 전에 쓰던거랑 똑같이 적어도 아무 상관 없는데....
        # rest_framework가 편의를 위해서... 조금 추가한 기능이 있다.
        # 이제는 우리가 RESTful한 API를 만들기 위해서는
        # 각 요청 (C, R, U, D) 에 따라서 서로 다른 METHOD로 구분해야한다.
        # 그래서, 생성 (POST), 수정(PUT/PATCH), 조회(GET)
            # 야, 어차피 `데이터`가 오는거 아님?
            # request.data에서 받으면안됨?
        serializer = TodoSerializer(data=request.data)
        # 유효성 검사 통과 못헀다는 소리는? 사용자가 데이터 잘못넣었단말아님?
        # 그럼, 유효성 검사 통과 못할때는 무저간 아무튼 400번대 에러아님?
        # 근데 이걸 왜 내가 매번 조건분기해서 따로 처리해줘야함?
        # 그냥 유효성 검사할때 처리하면 안됨?
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 사용자가 게시글을 `생성` 해달라고 했고
            # 생성에 성공했다면. 궁금하곘죠? 완성된 데이터의 모양이 어떨지?
            # 그거 반환해주면됨. + 조금 더 친절하게
            # 선생님의 `생성 요청이` 성공했다는 것을 알려주면 좋겠다.
                # 이제는 무슨 짓을하든 어쨋든 JSON이 반환되니까.
            # return Response(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
