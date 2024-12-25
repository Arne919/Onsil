from django import forms
from .models import TravelBucketList


class TravelBucketListForm(forms.ModelForm):
    class Meta:
        model = TravelBucketList
        # fields = '__all__'
        # 생긴게 이상해요 -> 파이썬은 오소 여러개를 하나의 변수에 할당하려고 하면 () 튜플로 묶어준다.
        # fields = 'destination_name', 'country', 'image', 'planned_visit_date', 'priority'
        # fields = ['destination_name', 'country', 'image', 'planned_visit_date', 'priority']
        # fields = ('destination_name', 'country', 'image', 'planned_visit_date', 'priority')
        # fields = {'destination_name', 'country', 'image', 'planned_visit_date', 'priority'}
        exclude = ('city', 'reason')
        widgets = {
            'destination_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
            'planned_visit_date': forms.DateInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
