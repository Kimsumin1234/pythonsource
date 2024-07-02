from django.db import models
from django.contrib.auth.models import User

# taggit (2024-07-02)
from taggit.managers import TaggableManager


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
    # taggit (2024-07-02) 추가후 migrate 한후 admin 페이지에 Posts 추가에 들어가면 Tags: 항목이 생긴걸 확인가능
    # blog-post 테이블에는 tags 컬럼이 생성이 안되고 따로 taggit_tag, taggit_taggeditem 테이블이 새로 생성된다
    # admin 페이지에서 태그를 넣고 새글을 작성하고 SQLite 를 확인해 보면 taggit_tag 에는 키워드(중복허용X), taggit_taggeditem 에는 index 정보가 들어간다
    tags = TaggableManager()
    # 좋아요 기능 (2024-07-02)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    # models 에서 직접 Meta 로 정렬조건을 주면
    # 리스트 추출시 작성일자를 기준으로 자동으로 내림차순으로 정렬해서 추출해준다
    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    # user, post, content, created_at, modified_at
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일자")
    modified_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name="수정일자"
    )
    # 외래키 : Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "%s - %s" % (self.id, self.user)
