from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def list(request):
    # 전체 리스트 추출
    # post_list = Post.objects.all()
    # context = {"post_list": post_list}

    # 페이지 나누기 개념 추가
    post_list = Post.objects.all()

    page = request.GET.get("page", 1)

    paginator = Paginator(post_list, 5)

    page_obj = paginator.get_page(page)

    context = {"post_list": page_obj}
    return render(request, "blog/list.html", context)


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, "blog/post.html", context)


@login_required(login_url="common:login")
def create(request):
    if request.method == "POST":
        # 폼에 post 로 넘어오는 내용 담기 (이미지 파일은 request.FILES 이런식으로 담아야한다)
        form = PostForm(request.POST, request.FILES)
        # 폼 유효성 검증 (forms.py 에서 유효성검증이 걸림)
        if form.is_valid():
            # 유효성 통과하면 저장 (작성자 정보를 담아서 저장)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("blog:list")
    else:
        form = PostForm()

    return render(request, "blog/create.html", {"form": form})


@login_required(login_url="common:login")
def modify(request, post_id):
    # 수정할 글 찾기
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        # instance= 사용
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("blog:detail", post.id)
    else:
        # instance= 사용
        form = PostForm(instance=post)

    # form 에는 id 가 없기 때문에 post.id 를 사용하기 위해서 "post": post 를 담아가지고 간다
    return render(request, "blog/modify.html", {"form": form, "post": post})


@login_required(login_url="common:login")
def delete(request, post_id):
    # 삭제할 글 찾기
    post = get_object_or_404(Post, id=post_id)
    post.delete()

    return redirect("blog:list")
