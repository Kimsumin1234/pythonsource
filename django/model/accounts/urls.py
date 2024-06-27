from django.urls import path, reverse_lazy
from . import views

# django 에 로그인관련 내장된 views
# 로그인/로그아웃 views를 accounts 앱에 따로 안만들고 내장된 views 를 사용해서 로그인/로그아웃 가능
from django.contrib.auth import views as auth_views

app_name = "common"

urlpatterns = [
    # login 처리를 하는 view가 함수형뷰가 아니라 클래스뷰임
    # 클래스뷰를 함수형뷰 처럼 사용하려면 as_view() 사용
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # 스프링부트 에서는 비밀번호 변경하면 세션 날리고 다시 로그인 페이지로 보내는데
    # django 는 알아서 비밀번호 변경후 변경한 비밀번호로 다시 세션에 담아주기 때문에 세션을 안날려도 된다
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            # PasswordChangeView 를 컨트롤+클릭 으로 들어가서 코드 복사해옴 : 기본값 변경 가능
            #  - template_name = "registration/password_change_form.html" : 템플릿 이름
            #  - success_url = reverse_lazy("password_change_done") : 비밀번호 변경 성공후 이동하는 url 기본값, 변경 가능
            template_name="registration/password_change.html",
            success_url=reverse_lazy("index"),
        ),
        name="password_change",
    ),
    path("register/", views.register, name="register"),
    # 비밀번호 초기화 관련 view 들
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            # template_name="registration/password_reset_form.html",
            template_name="registration/password_reset.html",
            # 사용자 이메일로 보낼 텍스트 양식 설정
            email_template_name="registration/password_reset_email.txt",
            success_url=reverse_lazy("common:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html",
            success_url=reverse_lazy("common:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
