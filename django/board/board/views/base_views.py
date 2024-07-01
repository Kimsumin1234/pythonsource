from django.shortcuts import render, get_object_or_404
from board.models import Question

# 페이지 나누기 (Paginator, Page 클래스를 잘 활용하면 된다)
# https://docs.djangoproject.com/en/5.0/ref/paginator/ 참고
from django.core.paginator import Paginator

# Q 함수 (검색filter 조건 주기위함 , or 조건으로 데이터 조회 2024-07-01)
# Count 함수 : 정렬할때 추천수 세야해서
from django.db.models import Q, Count

# 클라이언트 ip 가져오기 (2024-07-01)
from tools.utils import get_client_ip

from board.models import QuestionCount


def question_list(request):
    # 전체 질문 추출(페이지나누기적용O, 검색기능적용X)
    # question_list = Question.objects.all()
    # question_list = Question.objects.order_by("-created_at")

    # 1. 페이지 나누기 적용
    # 1) 현재 페이지 번호 가져오기
    # => 'page',1 : 변수명은 page 로정하고 page 정보가 없으면 1 값을 적용한다
    # page = request.GET.get("page", 1)
    # 2) 리스트를 한페이지에 20개 씩 보여주기
    # paginator = Paginator(question_list, 20)
    # 3) 현재페이지에 데이터 담기?
    # page_obj = paginator.get_page(page)

    # context = {"question_list": question_list}
    # 4) 페이지 나누기 적용 후 보내기
    # context = {"question_list": page_obj}
    # return render(request, "board/question_list.html", context)

    # 2. 검색 기능 적용
    # question_list = Question.objects.order_by("-created_at")
    # page = request.GET.get("page", 1)
    # 검색어 가져오기 (검색기능 추가 2024-07-01)
    # keyword = request.GET.get("keyword", "")

    # 검색 키워드 설정 : 제목,내용,질문작성자,답변작성자
    # if keyword:
    # Question.objects.filter(Q(subject__icontains==keyword)|
    #     question_list = question_list.filter(
    #         Q(subject__icontains=keyword)
    #         | Q(content__icontains=keyword)
    #         | Q(author__username__icontains=keyword)
    #         | Q(answer__author__username__icontains=keyword)
    #     ).distinct()

    # paginator = Paginator(question_list, 20)

    # page_obj = paginator.get_page(page)

    # 검색데이터 + 정렬기준데이터 도 같이 보내기
    # context = {"question_list": page_obj, "page": page, "keyword": keyword}
    # return render(request, "board/question_list.html", context)

    # 3. 정렬 기능
    page = request.GET.get("page", 1)
    keyword = request.GET.get("keyword", "")

    # 정렬 기준 가져오기 (2024-07-01)
    so = request.GET.get("so", "")

    if so == "recommend":  # 추천 개수
        # annotate() : Question 테이블에 추천수 세서 num_voter 라는 컬럼명을 알아서 붙여서 해줘
        question_list = Question.objects.annotate(num_voter=Count("voter")).order_by(
            "-num_voter", "-created_at"
        )
    elif so == "popular":  # 답변 개수
        question_list = Question.objects.annotate(num_answer=Count("answer")).order_by(
            "-num_answer", "-created_at"
        )
    else:
        question_list = Question.objects.order_by("-created_at")

    if keyword:
        question_list = question_list.filter(
            Q(subject__icontains=keyword)
            | Q(content__icontains=keyword)
            | Q(author__username__icontains=keyword)
            | Q(answer__author__username__icontains=keyword)
        ).distinct()

    paginator = Paginator(question_list, 20)

    page_obj = paginator.get_page(page)

    # 검색데이터 + 정렬기준데이터 도 같이 보내기
    context = {"question_list": page_obj, "page": page, "keyword": keyword, "so": so}
    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    question = get_object_or_404(Question, id=qid)

    # 클라이언트 ip 가져오기 (2024-07-01)
    # 같은 ip 일경우 1번만 조회수 올라감
    ip = get_client_ip(request)
    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()
    if cnt == 0:
        # QuestionCount 객체 생성후 저장
        questionCount = QuestionCount(ip=ip, question=question)
        questionCount.save()
        # Question 객체에 view_cnt + 1 하기
        if question.view_cnt:
            question.view_cnt += 1
        else:
            question.view_cnt = 1
        question.save()

    # 페이지 정보 보내주기 (2024-07-01)
    page = request.GET.get("page", 1)
    keyword = request.GET.get("keyword", "")
    so = request.GET.get("so", "recent")

    # 페이지 정보 보내주기 (2024-07-01)
    context = {"question": question, "page": page, "keyword": keyword, "so": so}
    return render(request, "board/question_detail.html", context)
