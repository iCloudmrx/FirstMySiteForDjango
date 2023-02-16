from django.http import Http404
from django.shortcuts import get_list_or_404, render

from .models import Post


def post_detail(request, id):
    post = get_list_or_404(Post,
                           id=id,
                           status=Post.Status.PUBLISHED)

    return render(request,
                  'blog/post/detail.html',
                  {'posts': post})


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

# Create your views here.
