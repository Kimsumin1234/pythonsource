from django.shortcuts import render, redirect
from .forms import UserForm


# 회원가입
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("common:login")
    else:
        form = UserForm()

    return render(request, "common/register.html", {"form": form})
