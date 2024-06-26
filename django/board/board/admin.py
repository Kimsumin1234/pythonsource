from django.contrib import admin
from .models import Question, Answer

# 이렇게 모델을 등록해야 admin 페이지에 추가된다
admin.site.register(Question)
admin.site.register(Answer)
