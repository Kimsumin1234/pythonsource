from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    # http://127.0.0.1:8000/blog/
    path("", views.list, name="list"),
    # http://127.0.0.1:8000/blog/post/1
    path("post/<int:post_id>/", views.detail, name="detail"),
    # http://127.0.0.1:8000/blog/post/create
    path("post/create/", views.create, name="create"),
    # http://127.0.0.1:8000/blog/post/modify/1
    path("post/modify/<int:post_id>/", views.modify, name="modify"),
    # http://127.0.0.1:8000/blog/post/delete/1
    path("post/delete/<int:post_id>/", views.delete, name="delete"),
]

# 댓글
urlpatterns += [
    # http://127.0.0.1:8000/blog/post/comment/<post_id>
    path("post/comment/<int:post_id>/", views.comment_create, name="comment_create"),
]

# 좋아요
urlpatterns += [
    # http://127.0.0.1:8000/blog/post/like/<post_id>
    path("post/like/<int:post_id>/", views.post_like, name="post_like"),
]
