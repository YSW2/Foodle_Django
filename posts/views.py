from django.shortcuts import render, redirect
from posts.forms import PostForm
from posts.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import random
# Create your views here.

def posts_view(request):
    posts = Post.objects.all()
    page = request.GET.get('page')

    if page is None:
        page = 1

    paginator = Paginator(posts, 10)
    custom_page_range = range(((int(page)-1) // 10) * 10 + 1, min(paginator.num_pages, ((int(page)-1) // 10) * 10 + 10) + 1)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)

    context = {
        "posts": posts,
        "page_obj": page_obj,
        "paginator": paginator,
        "custom_page_range": custom_page_range,
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

def generate_post(request):
    for i in range(100):
        random_int = random.randint(1, 100)
        random_post = Post(
            title=f"게시글 제목 {random_int}",
            content=f"게시글 내용 {random_int}",
            tags='all',
            user=request.user,
        )
        random_post.save()

    return redirect("posts:posts")

def delete_all_posts(request):
    posts = Post.objects.all()
    posts.delete()

    return redirect("posts:posts")