from django.contrib import admin
from .models import Photo

# admin 페이지에서 Photo 모델을 관리하기 위해서 입력하는 코드
# Photo 모델은 models.py 에서 정의함
admin.site.register(Photo)
