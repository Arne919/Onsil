from django.shortcuts import redirect, render, get_object_or_404
from .models import Travel
from .forms import TravelForm

# Create your views here.

def index(request):
    travels = Travel.objects.all()
    context = {
        'travels':travels
    }
    return render(request,'travels/index.html',context)

def create(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid:
            travel = form.save()
            return redirect('travels:detail',travel.pk)
    else:
        form = TravelForm()
    context={
        'form':form
    }
    return render(request,'travels/create.html',context)

def detail(request,pk):
    travel = get_object_or_404(Travel,pk=pk)
    context = {
        'travel':travel
    }
    return render(request,'travels/detail.html',context)

