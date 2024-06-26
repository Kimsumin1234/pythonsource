from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

# 페이지 나누기 (Paginator, Page 클래스를 잘 활용하면 된다)
# https://docs.djangoproject.com/en/5.0/ref/paginator/ 참고
from django.core.paginator import Paginator


def question_list(request):
    # 전체 질문 추출

    # question_list = Question.objects.all()
    question_list = Question.objects.order_by("-created_at")

    # 페이지 나누기 적용
    # 1) 현재 페이지 번호 가져오기
    # => 'page',1 : 변수명은 page 로정하고 page 정보가 없으면 1 값을 적용한다
    page = request.GET.get("page", 1)
    # 2) 리스트를 한페이지에 20개 씩 보여주기
    paginator = Paginator(question_list, 20)
    # 3) 현재페이지에 데이터 담기?
    page_obj = paginator.get_page(page)

    # context = {"question_list": question_list}
    # 4) 페이지 나누기 적용 후 보내기
    context = {"question_list": page_obj}
    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    question = get_object_or_404(Question, id=qid)
    context = {"question": question}
    return render(request, "board/question_detail.html", context)


# 답변등록
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
            answer.save()
            return redirect("board:question_detail", qid=qid)
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


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("board:question_list")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html", {"form": form})
