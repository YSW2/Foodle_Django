from django.urls import path
from posts.views import posts_view, post_add, post_detail

app_name = "posts"
urlpatterns = [
    path("posts/", posts_view, name="posts"),
    path("add/", post_add, name="post_add"),
    path("<int:post_id>/", post_detail, name="post_detail"),
]