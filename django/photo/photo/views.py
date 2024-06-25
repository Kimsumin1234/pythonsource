from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm


# 수정
def edit(request, id):
    # 수정할 내용 찾기
    photo = get_object_or_404(Photo, id=id)

    if request.method == "POST":
        # request.POST : 사용자 입력값
        # instance= : 모델폼에 찾은 내용 연결
        form = PhotoForm(request.POST, instance=photo)

        if form.is_valid():
            form.save()
            return redirect("photo_detail", id=id)
    else:
        # instance= : 생성은 비어있는 모델폼을 보내지만 수정은 찾은걸 연결시켜서 보내야한다
        form = PhotoForm(instance=photo)

    return render(request, "photo/photo_edit.html", {"form": form})


# 삭제
def remove(request, id):
    photo = get_object_or_404(Photo, id=id)
    photo.delete()
    return redirect("photo_list")


def detail(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, "photo/photo_detail.html", {"photo": photo})


# ModelForm 적용 (생성,수정 작업은 모델폼 사용하는게 편하다)
def create(request):
    if request.method == "POST":
        # 이렇게 하면 사용자가 입력한 내용을 PhotoForm 에 다 담을수있다
        # title = request.POST.get("title") 이거를 다 안적어도 됨
        form = PhotoForm(request.POST)

        # 유효성검증, 모델에 정의된 규칙에 따라서 검증을 해준다
        #  - 정의된 규칙 : max_length, required
        if form.is_valid():

            # model.save() 도 같이 호출됨
            form.save()
            return redirect("photo_list")
    else:
        form = PhotoForm()

    return render(request, "photo/photo_create.html", {"form": form})


def list(request):
    # pass
    # pass 만 있는경우 이런 에러메세지 화면이 출력
    # => The view photo.views.list didn't return an HttpResponse object. It returned None instead.

    photos = Photo.objects.all()
    return render(request, "photo/photo_list.html", {"photos": photos})
