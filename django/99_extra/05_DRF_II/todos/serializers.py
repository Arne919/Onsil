from rest_framework import serializers
from .models import Todo, Recommend


# todo 상세 조회 과정에서 이 todo를 참조하고있는 recommend들을 불러봐야한다.
# django에서 1의 입장이 자신을 참조하고 있는 N들을 불러오려면 어떻게 해야하나?
# recommend_set 이라고 하는 역참조 매니저를 통해서 가져온다.
class TodoSerializer(serializers.ModelSerializer):
    class RecommendForTodoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Recommend
            # fields = '__all__'
            # read_only_fields = ('todo',)
            exclude = ('todo',  )
    # serializer의 역할은, 각 field가 어떤 데이터를 어떻게 보여줄지를 정하는것.
    # recommend -> N개의 데이터, 즉 many=True 일 수 있다
    # TodoSerializer는 todo를 생성 할 떄도 쓰고있는데...
        # 이제 필드에 recommend_set 이 추가가 되면
        # 사용자가 todo를 생성하려고 할때도 recommend 정보를 넣어야 하는데
        # 그건... 이상한 거 같다.
    recommend_set = RecommendForTodoSerializer(many=True, read_only=True)
    class Meta:
        model = Todo
        fields = '__all__'

class TodoListSerializer(serializers.ModelSerializer):
    # Field를 정의한다 -> 내가 지금 보여주려고 하는 필드들에
        # 원래 Todo 모델이 가지고 있지 않았던 필드를 하나 더 추가 하고자한다.
        # Model에 없는 정보를 필드에 추가하려면? 무슨 데이터를 보여줄건지 정해야한다.
        # 즉, 이 필드를 위한 `소스` 가 무엇인지 알려줘야 한다.
    recommend_count = serializers.IntegerField(
        # data를 -> todo와 관련된 데이터를 -> 전처리 해서 -> int 형태로 
        # 즉, todo 입장에서 recommend에 대한 정보를 불러오는 방법
            # todo.recommend_set.querysetAPI
            # 이게 todo라는건 이미 적어놨음.
        source='recommend_set.count',
        read_only=True
    )
    class Meta:
        model = Todo
        fields = ('work', 'is_completed', 'recommend_count' )

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        # 어? 참조 대상 Todo는 지금은 사용자가 직접 선택 X
        '''
            read_only_fields를 사용해서 todo를 처리하고싶다면
            그 외에 다른 필드들은 어떻게 보여 줄것인지 작성해 줘야한다.
        '''
        fields = '__all__'
        # exclude = ('todo', )
        read_only_fields = ('todo', )