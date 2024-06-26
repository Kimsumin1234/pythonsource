from django.urls import path
from . import views

# 앱이름 (임의로 부여가능), 앱이 여러개가 들어올 경우, 각앱마다 동일한 name= 을 사용하면 다른걸 찾아올수 있어서 문제가 생길수있다
# 이러한 문제를 방지 하기위해서 앱이름도 추가하면 동일한 name= 을 문제없이 사용할수있다
# "{% url "board:question_detail" qid=question.id %}" 형태로 사용
app_name = "board"

urlpatterns = [
    # http://127.0.0.1:8000/board/
    path("", views.question_list, name="question_list"),
    # http://127.0.0.1:8000/board/1
    path("<int:qid>/", views.question_detail, name="question_detail"),
    # http://127.0.0.1:8000/board/answer/create/2 (뒤에 붙는 번호는 question_detail이 가지고 있는 질문번호)
    path("answer/create/<int:qid>/", views.answer_create, name="answer_create"),
    # http://127.0.0.1:8000/board/question/create/
    path("question/create/", views.question_create, name="question_create"),
]
