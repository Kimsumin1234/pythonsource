from django.db import models


# 테이블과 동일한 모델을 정의 class 로 작성
# class 코드를 작성한후 python manage.py makemigrations 명령어 입력
# todo\migrations\0001_initial.py 파일 생성
# python manage.py migrate 명령어 입력 하면 DB 에 테이블 생성
# DB Browser for SQLite 에 todo_todo(app이름_클래스명)테이블이 생성 PK 설정을 안하면 자동으로 id 변수가 만들어지고 PK 가 잡힌다


# 중간에 sql 코드를 변경해서 오류가 난다면 해결방법
# 1) migrations 폴더 날리고, db.sqlite3 파일을 날리고 서버재실행 하면된다
# 2) makemigrations, migrate 작업을 여러번 하면 0001 0002 0003 ... 이렇게 될텐데 수정한 작업까지 000 파일을 날리고 다시 작성?
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    # auto_now_add=True : 새글 등록시 자동으로 날짜 추가됨
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    # http://127.0.0.1:8000/admin/todo/todo/ 에서 게시판에 제목만 나오게하는 코드
    def __str__(self) -> str:
        return self.title
