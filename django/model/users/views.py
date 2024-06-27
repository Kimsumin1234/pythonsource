from django.shortcuts import render, redirect
from .forms import UserForm

# 로그인 관련 메소드 가 django 에 내장되있다
from django.contrib.auth import authenticate, login, logout


# 회원가입
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserForm()

    return render(request, "register.html", {"form": form})


# 로그인
# 사용자가 로그인 정보를 입력하면 입력한 정보를 담아서 DB 에 있는지 확인후 DB 에 있으면 session 에 담아서 로그인
# login() 이 이미 만들어져있기 때문에 이름을 바꿔서 common_login() 으로 사용해야 한다
def common_login(request):
    if request.method == "POST":
        # 사용자 로그인 입력값 가져오기
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 로그인 정보 담기
        # DB 에 로그인 정보가 있는지 확인 작업
        user = authenticate(request, username=username, password=password)

        # user 가 있으면 로그인
        if user is not None:
            # session 에 담는 작업
            login(request, user)
            return redirect("index")

    return render(request, "login.html")


# 그냥 로그인후 이동할 페이지 생성한것
def index(request):
    return render(request, "index.html")


# 로그아웃
def common_logout(request):
    logout(request)
    return redirect("index")
