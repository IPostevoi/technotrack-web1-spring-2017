from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Blog, Post
from comments.models import Comment
from django.views.generic import DetailView


def start(request):
    numb = len(Blog.objects.all())
    nump = len(Post.objects.all())
    numc = len(Comment.objects.all())
    return render(request, 'core/startPage.html', {"numberBlog": numb, "numberPost": nump, "numberComments": numc})

class CommentsList(DetailView):
    queryset = Post
    template_name = "comments.html"