from django.shortcuts import render
from .models import Garage

# Create your views here.
def index(request):
    # 차고지 전체 조회
    garages = Garage.objects.all()
    # 전체 목록을 html에서 그려야 해
    context = {
        'garages': garages
    }
    return render(request, 'garages/index.html', context)

def create(request):
    # 게시글 생성 해달라고 해서 해주는데... 이게맞나?
    garage = Garage()
    # 와 지금 필드 5갠데 이래?
    # PJT01때 필드 한 10개 됐던거 같은데? 그거 form태그 다적음?
    # 귀찮네?
    garage.location = request.GET.get('location')
    garage.capacity = request.GET.get('capacity')
    garage.is_parking_avaliable = request.GET.get('is_parking_avaliable')
    garage.opening_time = request.GET.get('opening_time')
    garage.closing_time = request.GET.get('closing_time')
    garage.save()
    # 게시글 생성 해달래ㅓ 해줬는데 뭐하지?
    return ??