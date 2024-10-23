from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .forms import LoginForm


User = get_user_model()

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:login')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    profile_owner = User.objects.get(username=username)
    like_diaries = profile_owner.diary_set.all()
    context = {
        'profile_owner': profile_owner,
        'like_diaries': like_diaries
    }
    return render(request, 'accounts/profile.html', context)

'''
    일반적으로 게시글과 같이 내가 직접 만믄 모델이라면, 그 모델 class 정보를
    from .models import Article >> 직접적으로 불러와도 된다.

    근데, User 모델은 조금 특별하게 대하기로 했었다.
    그래서, 지금 당장 User 모델 객체 자제가 필요한게 아니라면? 문자열로 대체
    from django.conf import settings
    settings.AUTH_USER_MODEL >> 'accounts.User'

    지금 당장 활성화 되어있는 User 모델 객체를 사용해야한다.
    from django.contrib.auth import get_user_model
    user = get_user_model().obje,~~~
'''
from django.contrib.auth import get_user_model
# 우리가 평소에 쓰는 모습이랑 비슷하게 만들어서 쓰면 될듯?
# 마치 PasCalCase로 작성한 class를 직접 가지고 온것처럼 그런 변수 하나 만들어서
# 거기에 get_user_model() 함수 호출한 결과 (활성화 되어있는 User 모델)
User = get_user_model()
def subscribe(request, user_pk):
    # 내가 저 사람을 이미 구독했다면, 내가 구독한 사람 목록에서 저 사람을 삭제
    # url을 통해 넘겨받은 user_pk로 특정 유저를 찾고자 한다.
    me = request.user
    you = User.objects.get(pk=user_pk)

    # 팔로우 할때와는 조금 다르게 한번 적어보자.
    # 나를 기준으로 적어보자.
    # 내가 구독을 하는거니까.
    # 저사람 내가 구독했었던 그 목록에 포함되어 있니?
    if you in me.subscription.all():
        # 이미 포함되어 있었다면? 난 구독을 취소하기 위한 요청을 보낸거야.
        me.subscription.remove(you)
    else:
        me.subscription.add(you)
    # 저 사람을 구독하고 있는 전체 목록을 출력하게 된다면,
    # 내가 저 사람을 구독하고 있다면, 내가 출력이 되겠죠
    print(you.subscriber.all()) 
    return redirect('accounts:profile', you.username)

