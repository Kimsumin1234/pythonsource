from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo

# 장고는 스프링부트 에서 사용했던 service가 없고 views 에서 해결한다

# 일반 문자열로 응답할 때는 이런식으로 작성한다
# def list(request):
#     return HttpResponse("Hello")


# html 로 응답할때 는 이런식으로 작성
def list(request):
    # 스프링부트에서 사용한 model.attribute() 랑 비슷한 개념
    # => todos = Todo.objects.all() , {'todos':todos}
    # => todo_list.html 에서 간단한 방법으로 {{todos}} 하면 호출할수있다
    # objects.all() 하면 todo 테이블 전체 컬럼을 다 가지고 들어온다 (SELECT * FROM 이랑 비슷한 개념)
    # todos = Todo.objects.all()
    # filter(completed=False) : completed 값이 False 인것만 list 페이지에 띄우기
    todos = Todo.objects.filter(completed=False)
    return render(request, "todo/todo_list.html", {"todos": todos})


# 완료된 Todo 목록
def done_list(request):
    dones = Todo.objects.filter(completed=True)
    return render(request, "todo/done_list.html", {"dones": dones})


def create(request):
    # get/post 둘다 처리
    # if 가 POST 면 post 아니면(else) get
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        important = request.POST.get("important")
        print("전송내용", title, description, important)

        if important:
            # 객체 생성
            todo = Todo(title=title, description=description, important=True)
        else:
            todo = Todo(title=title, description=description)
        todo.save()
        # redirect("urls.py 에 name에 적은 별칭 입력") : 스프링부트에 sendredirect() 와 같은개념
        return redirect("list")

    else:
        return render(request, "todo/todo_create.html")


# (request,id) : urls.py 에서 <int:id> 주소줄에 이런식으로 가기 때문에 id 변수를 추가해 준다
def read(request, id):
    # todo = Todo.objects.get(id=id)
    # get_object_or_404() 를 사용하면 오류메세지를 주르르륵 띄우지 않고 page not found 404 만 뜨게된다
    todo = get_object_or_404(Todo, id=id)
    return render(request, "todo/todo_detail.html", {"todo": todo})


# 수정
def edit(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == "POST":
        # 수정할 내용 찾기
        description = request.POST.get("description")
        important = request.POST.get("important")

        # 수정내용 삽입
        todo.description = description
        if important:
            todo.important = True
        else:
            todo.important = False

        # 저장
        todo.save()

        # read 할때 id 를 가지고 가야한다
        return redirect("read", id=id)

    else:
        return render(request, "todo/todo_edit.html", {"todo": todo})


# list 페이지 에서 완료 버튼 누르면 complited 값이 True 로 되게 하기
def done(request, id):
    # 수정할 model 찾기
    todo = Todo.objects.get(id=id)
    # 변경 내용 삽입
    todo.completed = True
    # 변경 내용 저장
    todo.save()
    return redirect("list")
