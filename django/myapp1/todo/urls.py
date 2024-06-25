# from 구문 복사붙여넣기
from django.urls import path
from . import views

# http://127.0.0.1:8000/todo/100/
# 없는 주소값을 입력하면 이런식으로 에러화면이 뜬다
# DoesNotExist at /todo/100/
# Todo matching query does not exist.

# url 치면 자동완성
# todo app views.py 가서 또 코딩 작성
# config urls.py에 path("todo/" 가 있어서 todo urls.py은 [path("", 로 그냥 둔다 (config urls.py 가 먼저 실행되기 때문에)
urlpatterns = [
    # views.list : views.py 에 있는 def list 호출
    # name="list" : 별칭 붙여놓는것
    # http://127.0.0.1:8000/todo/
    path("", views.list, name="list"),
    # http://127.0.0.1:8000/todo/create
    path("create/", views.create, name="create"),
    # http://127.0.0.1:8000/todo/1
    # <int:id> : <넘어올값타입:넘어올값컬럼>
    path("<int:id>/", views.read, name="read"),
    # http://127.0.0.1:8000/todo/edit/1
    path("edit/<int:id>/", views.edit, name="edit"),
    # http://127.0.0.1:8000/todo/done/1
    path("done/<int:id>/", views.done, name="done"),
    # http://127.0.0.1:8000/todo/done/
    path("done/", views.done_list, name="done_list"),
]
