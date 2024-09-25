from django.shortcuts import render
todo_list = []

# Create your views here.
def index(request):
    print(request.GET)
    work = request.GET.get('work')
    if work:
        todo_list.append(work)
    # print(work)
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')