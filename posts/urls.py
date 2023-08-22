from django.urls import path
from posts.views import posts_view

app_name = "posts"
urlpatterns = [
    path("posts/", posts_view, name="posts"),
]