from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

def create(request):
    return render(request, 'my_app/create.html')