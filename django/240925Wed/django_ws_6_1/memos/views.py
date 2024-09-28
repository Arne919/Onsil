from django.shortcuts import redirect, render, get_object_or_404
from .models import Memo
from .forms import MemoForm
from django.views.decorators.http import require_POST, require_http_methods, require_safe
# Create your views here.

def index(request):
    memos = Memo.objects.all()
    context = {
        "memos" : memos,
    }
    return render(request,"memos/index.html",context)

def create(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memo=form.cleaned_data.get('memo')
            summary=form.cleaned_data.get('summary')
            memo = Memo(memo=memo,summary=summary)
            memo.save()
            return redirect("memos:index")
    else:
        form = MemoForm()
    context = {
        'form' : form,
    }
    return render(request,'memos/create.html',context)

def detail(request,pk):
    memo = get_object_or_404(Memo,pk=pk)
    context = {
        'memo':memo,
    }
    return render(request,'memos/detail.html',context)

def delete(rquest,pk):
    memo = get_object_or_404(Memo,pk=pk)
    memo.delete()
    return redirect("memos:index")    