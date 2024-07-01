from django import forms

# user 생성 모델폼
# UserCreationForm 의 부모로 ModelForm 이 있음
# django 에서 User 를 사용하는방법
# => 1) django 가 제공하는 User 그대로 사용 (비밀번호 암호화를 자동으로 해줌)
# => 2) User 를 상속받고 새로 만든다 (암호화를 자동으로 안해준다던지 이러한 불편한점이 있음)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):

    # 아이디,비밀번호,비밀번호 확인은 자동으로 required 가 적용이 되고
    # 이메일은 자동으로 적용이 안됬는데 임의로 required 를 적용하는 방법
    email = forms.EmailField(label="이메일", help_text="사용할 이메일을 입력해 주세요")

    class Meta:
        model = User
        # fields = "__all__" 전부 가져오면 쓸데없는 내용들이 많이 들어있다
        # username : ID 개념
        # email : 이메일 주소
        # 비밀번호, 비밀번호 확인은 기본으로 가져온다
        fields = ["username", "email"]
        # http://127.0.0.1:8000/common/register/ 페이지에서 사용자 이름 => 아이디로 변경됨 (기본값은 username 을 그대로 변역해서 사용한다)
        labels = {"username": "아이디"}
