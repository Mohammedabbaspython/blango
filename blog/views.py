from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    ctx = {"posts": posts}
    return render(request, "blog/index.html", ctx)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    ctx = {"post": post}
    
    return render(request, "blog/post-detail.html", ctx)
