from django import forms
from .models import Todo
# Todo 를 위해서 사용자가 데이터를 입력해야 할
# Form tag를 구성해야 한다.
# 근데 Todo에 데이터 삽입하려면 필요한 컬럼 정보들
# 이미 우리가 class Todo에 다 적어놨다.
# 그래서 models.Todo 정보를 활용해서 Form을 만들거다
# 그러므로, Model 정보를 포함한 Form을 만들거다.
class TodoForm(forms.ModelForm):
    # Todo가 가지고 있는 모든 필드에 사용자가 값을 입력하면
    # 그 데이터로 todo 데이터를 생성한다!
    # 그걸 위한 form tag를 만들어준다.
    # work = forms.CharField(max_length=12)
    is_completed = forms.BooleanField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = Todo
        # fields = ('id', 'work', 'content',)
        fields = '__all__'
        # exclude = ('is_completed', )
        # is_completed에 값이 삽입은 되야해서 필드에서 제외 시키는게 아니라
        # 그냥 사용자한테서 안보이기만 하면 되겠다.
        
