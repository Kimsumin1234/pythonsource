from django.shortcuts import render, get_object_or_404, redirect
from board.models import Question, Answer
from board.forms import QuestionForm, AnswerForm

# 권한 설정 (2024-06-28)
from django.contrib.auth.decorators import login_required

# django 가 제공하는 시간 설정 (2024-06-28)
from django.utils import timezone

# a 태그 name 활용 (2024-06-28)
from django.shortcuts import resolve_url


# 답변등록
@login_required(login_url="common:login")
def answer_create(request, qid):
    # 생성하는 방법이 여러가지가 있다

    # 2) 모델폼을 이용하는 방법
    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # commit=False : 일단 DB 에 반영 하지 마시오
            answer = form.save(commit=False)
            # answer 에 question 을 담고 commit
            answer.question = question

            # 작성자 개념 추가 (2024-06-28)
            answer.author = request.user
            answer.save()
            # return redirect("board:question_detail", qid=qid)
            # detail 페이지의 특정 위치 로 이동하기 (a 태그 name 활용)
            return redirect(
                "{}#answer_{}".format(
                    resolve_url("board:question_detail", qid=qid), answer.id
                )
            )
    else:
        form = QuestionForm()

    # 실패 시 get 방식으로 처리 해야해서 render() 를 사용
    # 실패하고 다시 detail 페이지로 돌아올때 Question내용 + form 을 가지고 다시 돌아와야한다
    context = {"question": question, "form": form}
    return render(request, "board/question_detail.html", context)

    # 1) 모델을 직접 사용하는 방법
    # - 먼저 Question 을 찾는다
    # question = get_object_or_404(Question, id=qid)
    # - 1번 방법
    # answer = Answer.objects.create(
    #     question=question, content=request.POST.get("content")
    # )
    # - 2번 방법
    # question.answer_set.create(content=request.POST.get("content"))
    # - 3번 방법
    # answer = Answer(question=question, content=request.POST.get("content"))
    # answer.save()
    # - 앱이름 사용했기 때문에 board: 를 붙여준다
    # return redirect("board:question_detail", qid=qid)


# 답변 수정
@login_required(login_url="common:login")
def answer_modify(request, aid):
    # aid 에 해당하는 답변을 찾는다
    answer = get_object_or_404(Answer, id=aid)
    # Answer 가 question 을 가지고 있어서 .찍고 접근이 가능하다
    # question_detail 로 들어갈때는 qid 가 필요함
    qid = answer.question.id

    # 변경할 부분 수정 후 save()
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.modified_at = timezone.now()
            answer.save()
            # return redirect("board:question_detail", qid=qid)
            # detail 페이지의 특정 위치 로 이동하기 (a 태그 name 활용)
            return redirect(
                "{}#answer_{}".format(
                    resolve_url("board:question_detail", qid=qid), answer.id
                )
            )
    else:
        form = AnswerForm(instance=answer)

    return render(request, "board/answer_form.html", {"form": form})


# 답변 삭제
@login_required(login_url="common:login")
def answer_delete(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    answer.delete()

    # Answer 가 question 을 가지고 있어서 .찍고 접근이 가능하다
    qid = answer.question.id
    return redirect("board:question_detail", qid=qid)
