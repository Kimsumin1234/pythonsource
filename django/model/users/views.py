from django.shortcuts import render
from .forms import UserForm


# 회원가입
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()

    return render(request, "register.html", {"form": form})


# 로그인
# login() 이 이미 만들어져있기 때문에 이름을 바꿔서 common_login() 으로 사용해야 한다
def common_login(request):
    pass
