from django.shortcuts import render
from .models import Blog, Post
#from django.shortcuts import render
from django.views.generic import ListView, DetailView


class BlogsList(ListView):

    queryset = Blog.objects.all()
    template_name = 'posts/blogs.html'


class PostsList(ListView):

    queryset = Post.objects.all()
    template_name = 'posts/posts.html'


class BlogPage(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'


class CommentsList(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/comments.html'


class PostComments(DetailView):

    queryset = Post.objects.all()
    template_name = 'posts/PostComments.html'


#def show_blog(request, blog_id=None):
  #  blog = Blog.objects.get(id=blog_id)
  #  return render(request, "posts/blog.html", {'blog': blog})
