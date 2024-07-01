from django.shortcuts import render, get_object_or_404, redirect
from board.models import Question, Answer, Comment
from board.forms import CommentForm

# 권한 설정 (2024-06-28)
from django.contrib.auth.decorators import login_required

# django 가 제공하는 시간 설정 (2024-06-28)
from django.utils import timezone

# a 태그 name 활용 (2024-06-28)
from django.shortcuts import resolve_url


# 댓글(질문) 생성
@login_required(login_url="common:login")
def comment_create_question(request, qid):
    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # commit=False : 일단 DB 에 반영 하지 마시오
            comment = form.save(commit=False)
            # comment 에 question 을 담고 commit
            comment.question = question

            # 작성자 개념 추가 (2024-06-28)
            comment.author = request.user
            comment.save()
            # return redirect("board:question_detail", qid=qid)
            # detail 페이지의 특정 위치 로 이동하기 (a 태그 name 활용)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:question_detail", qid=qid), comment.id
                )
            )
    else:
        form = CommentForm()

    # 실패 시 get 방식으로 처리 해야해서 render() 를 사용
    # 실패하고 다시 detail 페이지로 돌아올때 Question내용 + form 을 가지고 다시 돌아와야한다
    context = {"question": question, "form": form}
    return render(request, "board/comment_form.html", context)


# 댓글(질문) 수정
@login_required(login_url="common:login")
def comment_modify_question(request, cid):
    # aid 에 해당하는 답변을 찾는다
    comment = get_object_or_404(Comment, id=cid)
    # Comment 가 question 을 가지고 있어서 .찍고 접근이 가능하다
    # question_detail 로 들어갈때는 qid 가 필요함
    qid = comment.question.id

    # 변경할 부분 수정 후 save()
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("board:question_detail", qid=qid)
            # detail 페이지의 특정 위치 로 이동하기 (a 태그 name 활용)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:question_detail", qid=qid), comment.id
                )
            )
    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html", {"form": form})


# 댓글(질문) 삭제
@login_required(login_url="common:login")
def comment_delete_question(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    comment.delete()

    # Comment 가 question 을 가지고 있어서 .찍고 접근이 가능하다
    qid = comment.question.id
    return redirect("board:question_detail", qid=qid)


# 댓글(답변) 생성
@login_required(login_url="common:login")
def comment_create_answer(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # comment 에 question 을 담고 commit
            comment.answer = answer

            # 작성자 개념 추가 (2024-06-28)
            comment.author = request.user
            comment.save()
            # return redirect("board:question_detail", qid=answer.question.id)
            # detail 페이지의 특정 위치 로 이동하기 (a 태그 name 활용)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:question_detail", qid=answer.question.id),
                    comment.id,
                )
            )
    else:
        form = CommentForm()

    return render(request, "board/comment_form.html", {"form": form})


# 댓글(답변) 수정
@login_required(login_url="common:login")
def comment_modify_answer(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    # comment_create_answer 가 aid 를 가지고 와서 comment.question.id 는 null 이다 그래서 answer 를 한번 더 들어가야한다
    qid = comment.answer.question.id

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("board:question_detail", qid=qid)
            # detail 페이지의 특정 위치 로 이동하기 (a 태그 name 활용)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:question_detail", qid=qid), comment.id
                )
            )
    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html", {"form": form})


# 댓글(답변) 삭제
@login_required(login_url="common:login")
def comment_delete_answer(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    comment.delete()

    qid = comment.answer.question.id
    return redirect("board:question_detail", qid=qid)
