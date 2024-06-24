# from 구문 복사붙여넣기
from django.urls import path
from . import views

# url 치면 자동완성
# todo app views.py 가서 또 코딩 작성
# config 에 path("todo/" 가 있어서 [path("", 로 그냥 둔다 (config urls.py 가 먼저 실행되기 때문에)
urlpatterns = [path("", views.list, name="list")]
