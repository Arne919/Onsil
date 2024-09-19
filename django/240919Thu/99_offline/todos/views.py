from django.shortcuts import render
todo_list = []
# Create your views here.
def main(request):
    print(request.GET)
    # get 매서드는 찾는 key가 없으면 None을 반환한다.
    work = request.GET.get('work')
    if work:    # work에 값이 있을때만(사용자가 요청했을때만)
        todo_list.append(work)
    print(work)
    context = {
        'work': todo_list
    }
    # app_name/templates/ 까지는 내가 안적어도 알아서 찾아간다.
    # app_name/templates/*/*.html
    return render(request, 'todos/main.html', context)

def create(request):
    return render(request, 'todos/create.html')