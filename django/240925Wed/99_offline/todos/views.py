from django.shortcuts import render, redirect
# view함수에서 사용할 데코레이터들 중, http와 관련된 것들
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

# 함수 하나는 하나의 일을 해야 한다.
# 게시글 생성 기능과 게시글 생성 페이지 렌더링 2가지 일을 하는것 처럼 보이지만...
# `게시글 생성` 과 관련된 업무 하나 하는게 맞다.
# 경로도... /todos/create/ 경로가 2개의 일을 하는것 처럼 보이지만
    # GET /todos/create/
    # POST /todos/create/
        # 서로 완전히 다른 경로로 생각해야한다
def create(request):
    # POST 요청을 보낼 수 있는 방법은?
    # create.html의 form 태그를 통해서만 요청 보낼 수 있다.
    # 그러면 당연하게도, create.html 을 먼저 렌덜링 해줘야한다.
    if request.method == 'POST':
        # 실제 게시글 생성
        form = TodoForm(request.POST)
        # print(form)
        if form.is_valid(): # 유효성 검사 통과시
            form.save()
            return redirect('todos:index')
    else:
        # GET 방식 요청일 때 무엇을 할것이냐?
        form = TodoForm()
    context = {
        'form': form
    }
    # create.html을 사용자에게 반환
    return render(request, 'todos/form.html', context)

# 데코레이터
@require_POST
def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    # 하드코딩 안한다/.
    # return redirect('/todos/index/')
    return redirect('todos:index')

def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo_pk)
    else:
        # GET 방식일떄. html 렌더링
        form = TodoForm(instance=todo)
    context = {
        'form': form
    }
    return render(request, 'todos/form.html', context)
