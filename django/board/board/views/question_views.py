from django.shortcuts import render, get_object_or_404, redirect
from board.models import Question
from board.forms import QuestionForm

# 권한 설정 (2024-06-28)
from django.contrib.auth.decorators import login_required

# django 가 제공하는 시간 설정 (2024-06-28)
from django.utils import timezone


# @login_required : 권한설정,로그인한 유저만 작성가능(2024-06-28)
# (login_url="common:login") : 권한이 없으면 로그인 페이지로 보낸다
@login_required(login_url="common:login")
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            # form.save()

            # 작성자 = 로그인유저 개념 추가 (2024-06-28)
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect("board:question_list")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html", {"form": form})


# 질문수정
@login_required(login_url="common:login")
def question_modify(request, qid):
    # qid 에 해당하는 질문을 찾는다
    question = get_object_or_404(Question, id=qid)

    # 변경할 부분 수정 후 save()
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            question = form.save(commit=False)
            question.modified_at = timezone.now()
            question.save()
            return redirect("board:question_detail", qid=qid)
    else:
        form = QuestionForm(instance=question)

    return render(request, "board/question_form.html", {"form": form})


# 질문삭제
@login_required(login_url="common:login")
def question_delete(request, qid):
    # qid 에 해당하는 질문을 찾는다
    question = get_object_or_404(Question, id=qid)

    question.delete()
    return redirect("board:question_list")
