from django.shortcuts import render, redirect
from posts.forms import PostForm
# Create your views here.

def posts_view(request):
    return render(request, "posts/posts.html")

def post_add(request):
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