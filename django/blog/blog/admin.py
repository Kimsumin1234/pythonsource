from django.contrib import admin
from .models import Post

# Post 모델 admin 페이지에 등록후 관리자 페이지에서 리스트글 5개 정도 작성함
admin.site.register(Post)
