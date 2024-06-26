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


# 2024-06-26
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.instrument


# 테이블 관계
class Album(models.Model):
    # artist 라는 컬럼은 Musician 값이 들어온다 (Musician 1명이 Album 을 여러장 발매 가능 외래키 형성)
    # 외래키 제약 조건 : on_delete=models.CASCADE (부모(Musician)삭제 하면 자식(Album)도 같이 삭제됨)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self) -> str:
        # artist.first_name : 스프링부트 와 똑같이 .찍고 접근 가능 (N -> 1 쪽으로 접근 방법)
        return self.artist.first_name + " " + self.name


# shell
# from app1.models import Musician,Album

# Musician.objects.create(first_name='abc',last_name='def',instrument='piano')
# => <Musician: abc def piano>

# Musician.objects.create(first_name='hij',last_name='ttt',instrument='accordion')
# => <Musician: hij ttt accordion>

# Album.objects.create(artist=Musician.objects.get(id=1),name='flower',release_date='2024-06-26',num_stars=2)
# => <Album: abc flower>

# musician = Musician.objects.get(id=2)
# Album.objects.create(artist=musician,name='flower',release_date='2024-06-26',num_stars=2)
# => <Album: hij flower>

# Musician.objects.all()
# => <QuerySet [<Musician: abc def piano>, <Musician: hij ttt accordion>]>

# Musician.objects.count()
# => 2

# Album.objects.order_by('release_date') 오름차순?
# => <QuerySet [<Album: abc flower>, <Album: hij flower>]>

# Album.objects.order_by('release_date') 내림차순?
# => <QuerySet [<Album: abc flower>, <Album: hij flower>]>

# list(Musician.objects.all())
# => [<Musician: abc def piano>, <Musician: hij ttt accordion>]

# Musician.objects.exclude(instrument='piano')
# => <QuerySet [<Musician: hij ttt accordion>]>


class Fruit(models.Model):
    # PK 를 따로 명시를 안하면 id 라는 컬럼이 자동으로 생성되고 시퀀스값이 자동으로 들어간다
    # primary_key=True : id 를 pk 로 안쓰고 따로 PK 를 명시
    name = models.CharField(max_length=100, primary_key=True)
