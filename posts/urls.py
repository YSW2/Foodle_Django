from django.urls import path
from posts.views import posts_view, post_add, post_detail, generate_post, delete_all_posts, like_this_post, comment_add, post_delete, comment_delete

app_name = "posts"
urlpatterns = [
    path("", posts_view, name="posts"),
    path("add/", post_add, name="post_add"),
    path("<int:post_id>/post_delete/", post_delete, name="post_delete"),
    path("<int:post_id>/", post_detail, name="post_detail"),
    path("generate_post/", generate_post, name="generate_post"),
    path("delete_all_posts/", delete_all_posts, name="delete_all_posts"),
    path("<int:post_id>/like/", like_this_post, name="like_this_post"),
    path("add/", comment_add, name="comment_add"),
    path("<int:comment_id>/comment_delete/", comment_delete, name="comment_delete")
]