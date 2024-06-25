from django.db import models

# ORM 의 장점
# DB 를 도중에 바꿔도 된다
# 지금은 내장 DB SQLite 를 쓰고있지만 oracle, mybatis 로도 자유롭게 변경이 가능
# 화면단에서 text(단문) 로 입력하는거는 CharField() 로 만들고 max_length 로 크기 지정 을 해야한다
# 화면단에서 textArea(장문) 로 입력하는거는 TextField() 로 한다 이건 따로 크지 지정을 안한다


class Photo(models.Model):
    # 이렇게만 작성하면 필수요소 가 자동으로 설정 (required 비어있으면안됨)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()

    # http://127.0.0.1:8000/admin/photo/photo/ 페이지 에서 def __str__ 가 없으면 Photo object 가 기본값이다
    def __str__(self) -> str:
        return self.title
