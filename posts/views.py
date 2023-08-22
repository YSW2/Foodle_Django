from django.shortcuts import render

# Create your views here.

def posts_view(request):
    return render(request, "posts/posts.html")