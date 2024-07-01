from django.db import models
from django.contrib.auth.models import User


# auto_now_add : 처음 생성할때 한번만 시간이 설정
# auto_now : 생성,수정 할때마다 시간 설정
# upload_to="image" : 이미지 파일을 업로드 할수있게 해줌
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to="image")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # models 에서 직접 Meta 로 정렬조건을 주면
    # 리스트 추출시 작성일자를 기준으로 자동으로 내림차순으로 정렬해서 추출해준다
    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title
