from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth import views as auth_views

# model 프로젝트에 accounts 앱에 urls.py 에서 코드 복사해옴
# => registration/ 경로 잡힌걸 모두 common/ 경로로 변경

app_name = "common"

urlpatterns = [
    path(
        "login/",
        # common 폴더 밑에 login.html 이 있음
        auth_views.LoginView.as_view(template_name="common/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="common/password_change.html",
            success_url=reverse_lazy("index"),
        ),
        name="password_change",
    ),
    path("register/", views.register, name="register"),
    # 비밀번호 초기화 관련 view 들
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="common/password_reset.html",
            email_template_name="common/password_reset_email.txt",
            success_url=reverse_lazy("common:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="common/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="common/password_reset_confirm.html",
            success_url=reverse_lazy("common:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="common/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
