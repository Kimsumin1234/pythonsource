"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# settings.py 설정
# settings.py 에서 INSTALLED_APPS = [ "todo", ] 입력
# 데이타베이스 종류 변경하고 싶으면 : DATABASES = { } 여기서 변경
# 사이트 영어로 뜨는거 를 한글로 바꾸고 싶으면 : LANGUAGE_CODE = 'en-us' -> 'ko-kr' 변경
# TIME_ZONE = 'UTC' -> 'Asia/Seoul' 변경

from django.contrib import admin
from django.urls import path, include  # include 작성

urlpatterns = [
    # 관리자 페이지 자동 생성
    path("admin/", admin.site.urls),
    # todo/ 로 들어오는 경로요청은 todo 앱의 urls 파일이 담당
    # path('blog/', include('blog.urls')) 위에 코드 복사 붙여넣기후 blog 에 app 이름 넣음
    path("todo/", include("todo.urls")),
]
