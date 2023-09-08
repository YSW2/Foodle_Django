from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.views.decorators.http import require_POST
import random
# Create your views here.

def posts_view(request):
    page = request.GET.get('page')
    name = request.GET.get('name')
    keyword = request.GET.get('keyword')

    page_num = 10   #한 번에 표시할 페이지의 갯수

    if page is None:
        page = 1

    if name == 'title':
        posts = Post.objects.filter(title__icontains=keyword).order_by('-created')
    elif name == 'content':
        posts = Post.objects.filter(content__icontains=keyword).order_by('-created')
    elif name == 'title_content':
        posts = Post.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword)).order_by('-created')
    else:
        posts = Post.objects.order_by('-created')

    paginator = Paginator(posts, page_num)
    custom_page_range = range(((int(page)-1) // page_num) * page_num + 1, min(paginator.num_pages, ((int(page)-1) // page_num) * page_num + page_num) + 1)

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

@require_POST
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)

    if post.user == request.user:
        post.delete()

    else:
        HttpResponseForbidden("삭제 권한이 없습니다")

    return redirect("posts:posts")

@require_POST
def comment_add(request):
    if not request.user.is_authenticated:
        return redirect("users:login")

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

        return redirect("posts:post_detail", post_id=comment.post.id)

@require_POST
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    user = request.user

    if comment.user == user:
        comment.delete()

    return redirect("posts:post_detail", post_id=comment.post.id)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    if user.is_authenticated:
        if not post.views.filter(id=user.id).exists():
            post.views.add(user)

    comment_form = CommentForm()

    context = {
        "post": post,
        "comment_form": comment_form,
    }
    return render(request, "posts/post_detail.html", context)

@require_POST
def like_this_post(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    if user.like_posts.filter(id=post_id).exists():
        user.like_posts.remove(post)

    else:
        user.like_posts.add(post)

    url_next = request.GET.get("next")
    return redirect("posts:post_detail", post_id=post.id)

def generate_post(request):
    for i in range(100):
        random_post = Post(
            title=f"게시글 제목 {i+1}",
            content=f"게시글 내용 {i+1}",
            tags='all',
            user=request.user,
        )
        random_post.save()

    return redirect("posts:posts")

def delete_all_posts(request):
    posts = Post.objects.all()
    posts.delete()

    return redirect("posts:posts")