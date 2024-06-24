from django.db import models


# 테이블과 동일한 모델을 정의 class 로 작성
# 중간에 sql 코드를 변경해서 오류가 난다 하면 migrations 폴더 날리고, db.sqlite3 파일을 날리고 서버재실행 하면된다
# class 코드를 작성한후
# DB Browser for SQLite 에 todo_todo(app이름_클래스명)테이블이 생성 PK 설정을 안하면 자동으로 id 변수가 만들어지고 PK 가 잡힌다
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
