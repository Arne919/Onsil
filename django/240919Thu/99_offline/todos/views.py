from django.shortcuts import render

# Create your views here.
def main(request):
    # app_name/templates/ 까지는 내가 안적어도 알아서 찾아간다.
    # app_name/templates/*/*.html
    return render(request, 'todos/main.html')

def create(request):
    return render(request, 'todos/create.html')