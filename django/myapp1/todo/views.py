from django.shortcuts import render
from django.http import HttpResponse


# 일반 문자열로 응답할 때는 이런식으로 작성한다
# def list(request):
#     return HttpResponse("Hello")


# html 로 응답할때 는 이런식으로 작성
def list(request):
    return render(request, "todo/todo_list.html")
