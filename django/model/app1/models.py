from django.db import models


# 기본 테이블명은 프로젝트명_클래스명 이렇게 만들어진다 => app1_person
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # 테이블명 기본말고 직접정의
    # 모델이 수정됨 -> python manage.py makemigrations, python manage.py migrate 명령어 사용
    # 테이블명이 app1_person => person 으로 수정됨
    class Meta:
        db_table = "person"

    # def ~ : makemigrations 대상이 아님 (명령어 사용 안해도됨)
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
