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

from django.contrib import admin
from django.urls import include, path
from users.views import index

# django 에 로그인관련 내장된 views
# django.contrib.auth 패키지 안에 User 와 관련된 기능들이 내장되있다
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("users/", include("users.urls")), # 내가 만들어 놓은 login/,logout/ 주소와 django 내장되있는 주소와 겹쳐서 일단 막음
    # path("", index),
    # accounts/urls.py 에서 success_url=reverse_lazy("index"), 로 움직여야 해서 name="index" 를 추가함
    path("", index, name="index"),
    # path("accounts/", include("django.contrib.auth.urls")), # 따로 앱을 안만들고 이렇게 사용해도 django 가 제공하는 아래주석에 로그인관련 기능 사용가능
    path(
        "accounts/", include("accounts.urls")
    ),  # 앱을 통해서 django 가 제공하는 로그인관련 기능 사용해보기
]

# django 에 이러한 기능이 내장으로 구현 되있음
# => 회원가입, 로그인, 로그아웃, 비밀번호 변경, 비밀번호 초기화(이메일 이용해서 특정링크 보내기)
# path("accounts/", include("django.contrib.auth.urls")), 설정후
# http://127.0.0.1:8000/accounts/
# 이러한 url 이 자동으로 생성되있다
# accounts/ login/ [name='login'] =(로그인성공하면)=> http://127.0.0.1:8000/accounts/profile/ 이쪽으로 이동한다(기본으로 이렇게 셋팅이 되있음,settings에서 변경가능)
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change'] (비밀번호 변경 페이지)
# accounts/ password_change/done/ [name='password_change_done'] (비밀번호 변경 완료 페이지)
# accounts/ password_reset/ [name='password_reset'] (비밀번호 초기화 페이지)
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm'] (이상한 토큰값과 비밀번호 변경 주소를 이메일로 보냄)
# accounts/ reset/done/ [name='password_reset_complete']

# django 가 제공하는 로그인 기능 사용하기
# http://127.0.0.1:8000/accounts/login/ 치고 들어갔더니
# => registration/login.html 이경로로 찾았다
# settings.py 로 가서 "DIRS": [BASE_DIR / "templates"], 를 설정
# 저거를 설정해서 users/templates/login.html 로 가는게 아니라 model/templates/registration/login.html 로 가게 만듬

# django 가 제공하는 로그인/로그아웃 기능을 그대로 사용하면
# users/views.py 에 있는 common_login, common_logout 같은 함수를 따로 안만들어도 로그인/로그아웃 기능을 사용할수있다
