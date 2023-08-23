from django.urls import path
from posts.views import posts_view, post_add

app_name = "posts"
urlpatterns = [
    path("posts/", posts_view, name="posts"),
    path("add/", post_add, name="post_add"),
]