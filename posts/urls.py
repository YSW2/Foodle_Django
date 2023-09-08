from django.urls import path
from posts.views import posts_view, post_add, post_detail, generate_post, delete_all_posts, like_this_post

app_name = "posts"
urlpatterns = [
    path("", posts_view, name="posts"),
    path("add/", post_add, name="post_add"),
    path("<int:post_id>/", post_detail, name="post_detail"),
    path("generate_post/", generate_post, name="generate_post"),
    path("delete_all_posts/", delete_all_posts, name="delete_all_posts"),
    path("<int:post_id>/like/", like_this_post, name="like_this_post"),
]