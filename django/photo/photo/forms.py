from django import forms
from .models import Photo


# ModelForm : 모델과 연결된 form 선언
#             Photo 모델의 필드를 모두 가지고 있는 상태
#             class Meta: 는 무조건 써준다
#             views.py 에 가서 PhotoForm() 을 보내고
#             photo_create.html 에 가서 {{form}} 만 쓰면 자동으로 form 기본테이블이 만들어진다
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        # "__all__" : 모델에 있는 필드값 모두 사용한다
        fields = "__all__"
