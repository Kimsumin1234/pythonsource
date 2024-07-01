from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__" => 다가져오면 user 도 가져와버려서 User 필수 항목입니다. Valid 가 걸림
        # 생성할때 user 는 입력을 안하니깐 제외 시킨다
        fields = ["title", "content", "image"]
