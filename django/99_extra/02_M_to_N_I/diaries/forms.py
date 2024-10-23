from django import forms
from .models import Diary, Comment


class DiaryForm(forms.ModelForm):

    class Meta:
        model = Diary
        # 사용자가 Diary를 생성,수정 하기위한
        # form을 구성할때, 어떤 field들로 채울것이냐.
        # fields = '__all__'
        # fields = ('content', 'picture',)
        exclude = ('like_users', )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ('content',)
        exclude = ('diary',)