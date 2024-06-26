from django.db import models

# auto_now_add= : 가장 처음 삽입시 에만 날짜와 시간 삽입
# auto_now= : 수정할 때마다 날짜와 시간 변경
# null=True, blank=True : 데이터값이 비어있어도 됨, 같이써야 된다, 안주면 notnull 조건이 자동으로 적용


class Question(models.Model):
    # verbose_name= : 이거를 주면 admin 페이지에서 Questions 에 +추가 들어가면
    # 기본은 컬럼명이 나오지만 Content: , verbose_name="내용" 을 주면 내용: 으로 나온다
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")

    def __str__(self):
        return self.content
