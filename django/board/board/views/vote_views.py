from django.shortcuts import get_object_or_404, redirect
from board.models import Question, Answer

# 권한 설정 (2024-06-28)
from django.contrib.auth.decorators import login_required

# 메시지 보내기 (2024-06-28)
from django.contrib import messages


# 질문 추천
@login_required(login_url="common:login")
def vote_question(request, qid):
    question = get_object_or_404(Question, id=qid)

    # 내가 작성한 글은 추천못함
    # question.author(질문작성자), request.user(로그인유저)
    if question.author == request.user:
        # django 가 제공하는 메세지 보내는 기능으로 화면단에 메세지를 보낼수 있다 (스프링에서는 비슷하게 Flashattr 방식을 썻었음)
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        # voter 모델을 안만들어서
        # add() 가 자동으로 같은 id 가 중복으로 추천하는것도 막아준다
        question.voter.add(request.user)
    return redirect("board:question_detail", qid)


# 답변 추천
@login_required(login_url="common:login")
def vote_answer(request, aid):
    answer = get_object_or_404(Answer, id=aid)

    # 내가 작성한 글은 추천못함
    # question.author(질문작성자), request.user(로그인유저)
    if answer.author == request.user:
        # django 가 제공하는 메세지 보내는 기능으로 화면단에 메세지를 보낼수 있다 (스프링에서는 비슷하게 Flashattr 방식을 썻었음)
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        # voter 모델을 안만들어서
        # 자동으로 같은 id 가 중복으로 추천하는것도 막아준다
        answer.voter.add(request.user)
    return redirect("board:question_detail", qid=answer.question.id)
