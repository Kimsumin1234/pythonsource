from django.db import models
from django.contrib.auth.models import User  # 2024-06-28

# auto_now_add= : 가장 처음 삽입시 에만 날짜와 시간 삽입
# auto_now= : 수정할 때마다 날짜와 시간 변경
# null=True, blank=True : 데이터값이 비어있어도 됨, 같이써야 된다, 안주면 notnull 조건이 자동으로 적용


# 질문
class Question(models.Model):
    # verbose_name= : 이거를 주면 admin 페이지에서 Questions 에 +추가 들어가면
    # 기본은 컬럼명이 나오지만 Content: , verbose_name="내용" 을 주면 내용: 으로 나온다
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    # 작성자 추가 (2024-06-28)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 추천 개념 추가 (2024-06-28) : voter
    # User : user 가 추천을 한다
    # class Question(models.Model) 이 지금 (User, 가 2번 쓰인 상황이라서 에러가 발생한다
    # Question 입장에서는 question.author 와 question.voter 로 구별이 되지만,
    # User 입장에서 Question 으로 접근하려고 하면 User.question_set 이 author 인지 voter 인지 구별이 되지 않아서
    # makemigrations 하면 SystemCheckError: System check identified some issues: 에러가 뜬다
    # 해결방법 접근할때 이름을 정해서 구별해준다 : related_name=
    # 해결을 하고 makemigrations 하면 ManyToManyField 다대다 관계이기 때문에 SQLite 로 가면 board_question_voter 테이블이 새로 생성이 된다
    voter = models.ManyToManyField(User, related_name="voter_question")
    # 조회수기능 추가 (2024-07-01)
    view_cnt = models.BigIntegerField(default=0)

    def __str__(self):
        return self.subject


# 답변
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    # 작성자 추가 (2024-06-28)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 추천 개념 추가 (2024-06-28)
    voter = models.ManyToManyField(User, related_name="voter_answer")

    def __str__(self):
        return self.content


# 댓글
# 지금까지는 답변댓글 따로 질문댓글 따로 해서 테이블을 2개 만들었지만
# 여기서 해보는건 댓글테이블 1개만 만들어서 외래키를 질문,댓글 2개로 잡아서 처리해보기
# null=True, blank=True : 이걸 설정해서 필수입력 요소를 제외한다
# Comment 모델 순서 : Question, Answer 모델을 찾으려면 아래에다가 작성해야함
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    # 외래키 : 질문,댓글 설정
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True, blank=True
    )
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)


# 조회수 기능에 사용할 ip 기록 (2024-07-01)
class QuestionCount(models.Model):
    ip = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __unique__(self):
        return self.io
