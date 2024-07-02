from django.contrib import admin
from .models import Post, Comment

# Post 모델 admin 페이지에 등록후 관리자 페이지에서 리스트글 5개 정도 작성함
# 심플한 admin 관리자 페이지 형태 (models.py 에 정의한 def __str__(self) -> str: 형태로 리스트가 출력됨)
# admin.site.register(Post)
# admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
    # 이런식으로 하면 원하는 컬럼명을 사용해서 admin 페이지 리스트 출력 가능
    list_display = ("title", "created_at")
    # 링크를 걸고 싶은 컬럼 지정 가능
    list_display_links = ["title"]
    # admin 페이지 검색기능 활성화
    search_fields = ["title"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
