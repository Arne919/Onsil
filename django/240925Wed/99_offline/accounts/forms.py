# 파일명 forms.py 아니어도 됩니다.
from django import forms

# Form, ModelForm
# 공통점
    # class Form 무엇을 위한 것이냐?
    # 모든 Form을 위한 설정을 정의 하는 곳.
        # -> HTML Form tag를 어떻게 만들 것이냐?
        # 즉, 사용자가 입력할 input tag들을 어떻게 정의할 것이냐.
class LoginForm(forms.Form):
    # 마치 모델 정의 했었던 것처럼
    # username은 문자열을 입력받을 수 있는데, 12글자 제한이야.
    username = forms.CharField(max_length=12)
    # password는 문자열인데, 비밀번호를 입력받을 공간이야.
        # HTML에서 만들어질 input 태그가 어떤 모양이 될건지 추가 옵션정의
    password = forms.CharField(widget=forms.PasswordInput())