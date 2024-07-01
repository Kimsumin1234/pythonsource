"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# 파일 업로드 관련
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("common/", include("common.urls")),
    path("", RedirectView.as_view(url="blog/"), name="index"),
]

# settings.py 에 설정한것 불러오기(MEDIA_URL, MEDIA_ROOT)
# blog 프로젝트 밑에 media 폴더가 자동으로 생성되고 업로드한 이미지들이 media 폴더에 추가된다
# http://127.0.0.1:8000/media/image/python.png 경로는 이런식으로 만들어짐
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
