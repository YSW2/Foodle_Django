from django.shortcuts import render, redirect
from posts.forms import PostForm
from posts.models import Post
# Create your views here.

def posts_view(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "posts/posts.html", context)

def post_add(request):
    if not request.user.is_authenticated:
        return redirect("users:login")

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect("posts:posts")

    else:
        form = PostForm()

    context = {
        "form": form
    }
    return render(request, "posts/post_add.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post,
    }
    return render(request, "posts/post_detail.html", context)