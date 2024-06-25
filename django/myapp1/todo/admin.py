from django.contrib import admin
from .models import Todo

# admin 사이트에서 관리할 모델을 등록
# http://127.0.0.1:8000/admin/ 로 들어가보면 사이트관리 목록에 Todos 가 생긴다
# Todos 옆에 +추가 를 누르면 게시글 추가하는 사이트가 나온다
# 제목 내용 입력하고 저장을 누르고 SQLite 에 todo_todo DB 를 살펴보면 데이터가 들어가 있다
# 생성된 데이터의 컬럼들은 models.py 에서 정의한것
admin.site.register(Todo)
