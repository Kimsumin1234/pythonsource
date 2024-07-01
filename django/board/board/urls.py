from django.urls import path

# from . import views
# views 폴더 만들어서 views 별로 나눴음
from .views import base_views, question_views, answer_views, comment_views, vote_views

# 앱이름 (임의로 부여가능), 앱이 여러개가 들어올 경우, 각앱마다 동일한 name= 을 사용하면 다른걸 찾아올수 있어서 문제가 생길수있다
# 이러한 문제를 방지 하기위해서 앱이름도 추가하면 동일한 name= 을 문제없이 사용할수있다
# "{% url "board:question_detail" qid=question.id %}" 형태로 사용
app_name = "board"

urlpatterns = [
    # http://127.0.0.1:8000/board/
    path("", base_views.question_list, name="question_list"),
    # http://127.0.0.1:8000/board/1
    path("<int:qid>/", base_views.question_detail, name="question_detail"),
    # http://127.0.0.1:8000/board/answer/create/2 (뒤에 붙는 번호는 question_detail이 가지고 있는 질문번호)
    path("answer/create/<int:qid>/", answer_views.answer_create, name="answer_create"),
    # http://127.0.0.1:8000/board/question/create/
    path("question/create/", question_views.question_create, name="question_create"),
    # http://127.0.0.1:8000/board/question/modify/1
    path(
        "question/modify/<int:qid>",
        question_views.question_modify,
        name="question_modify",
    ),
    # http://127.0.0.1:8000/board/question/delete/1
    path(
        "question/delete/<int:qid>",
        question_views.question_delete,
        name="question_delete",
    ),
    # 답변 이라서 답변 id 를 찾아야 해서 <int:aid> 를 사용
    # http://127.0.0.1:8000/board/answer/modify/1
    path("answer/modify/<int:aid>", answer_views.answer_modify, name="answer_modify"),
    # http://127.0.0.1:8000/board/answer/delete/1
    path("answer/delete/<int:aid>", answer_views.answer_delete, name="answer_delete"),
    # 댓글(질문), <int:cid> 를 사용
    # http://127.0.0.1:8000/board/comment/create/question/1
    path(
        "comment/create/question/<int:qid>",
        comment_views.comment_create_question,
        name="comment_create_question",
    ),
    # http://127.0.0.1:8000/board/comment/modify/question/1
    path(
        "comment/modify/question/<int:cid>",
        comment_views.comment_modify_question,
        name="comment_modify_question",
    ),
    # http://127.0.0.1:8000/board/comment/delete/question/1
    path(
        "comment/delete/question/<int:cid>",
        comment_views.comment_delete_question,
        name="comment_delete_question",
    ),
    # 댓글(답변)
    # http://127.0.0.1:8000/board/comment/create/answer/1
    path(
        "comment/create/answer/<int:aid>",
        comment_views.comment_create_answer,
        name="comment_create_answer",
    ),
    # http://127.0.0.1:8000/board/comment/modify/answer/1
    path(
        "comment/modify/answer/<int:cid>",
        comment_views.comment_modify_answer,
        name="comment_modify_answer",
    ),
    # http://127.0.0.1:8000/board/comment/delete/answer/1
    path(
        "comment/delete/answer/<int:cid>",
        comment_views.comment_delete_answer,
        name="comment_delete_answer",
    ),
    # 추천 시스템
    # http://127.0.0.1:8000/board/vote/question/1 <question id> : 질문 추천
    path("vote/question/<int:qid>/", vote_views.vote_question, name="vote_question"),
    # http://127.0.0.1:8000/board/vote/answer/1 <answer id> : 답변 추천
    path("vote/answer/<int:aid>/", vote_views.vote_answer, name="vote_answer"),
]
