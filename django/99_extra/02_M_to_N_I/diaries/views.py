from django.shortcuts import render, redirect
from .models import Diary, Comment
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comment_form = CommentForm()
    context = {
        'diaries': diaries,
        'comment_form': comment_form
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def comments_create(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.diary = diary
            comment.save()
    return redirect('diaries:index')

def comments_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('diaries:index')

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# 1. 로그인 되어 있는 유저만 like가 가능해야한다.
@login_required
# 2. POST요청일 때만 가능해야 한다.
@require_POST
def likes(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    # if request.user.is_authenticated:
    #     if request.method == 'POST':
    # 3. 좋아요를 이미 눌렀냐 안눌렀냐에 따라서 하는일이 달라져야한다.
    if request.user in diary.like_users.all():
        diary.like_users.remove(request.user)
    else:
        diary.like_users.add(request.user)
    return redirect('diaries:index')

