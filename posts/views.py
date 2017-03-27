# -*- coding: utf-8 -*-
from .models import Blog, Post
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django import forms
from posts.forms import SortForm


class  UpdateBlog(UpdateView):

    template_name = "posts/editblog.html"
    model = Blog
    fields = ('title', 'description')
    success_url = '/blogs/list/'

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)


class CreateBlog(CreateView):

    template_name = "posts/addblog.html"
    model = Blog
    fields = ('title', 'description')
    success_url = '/blogs/list'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBlog, self).form_valid(form)


class UpdatePost(UpdateView):
    template_name = "posts/editpost.html"
    model = Post
    fields = ('title', 'text', 'blog')
    success_url = '/blogs/posts/list/'

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)


class CreatePost(CreateView):
    template_name = "posts/addpost.html"
    model = Post
    fields = ('title', 'text', 'blog')
    success_url = '/blogs/list'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(CreatePost, self).get_form()
        form.fields["blog"].queryset = Blog.objects.filter(author=self.request.user)
        return form


class BlogsList(ListView):

    queryset = Blog.objects.order_by('-time').all()
    template_name = 'posts/blogs.html'
    sortform = None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context

    def get_queryset(self):
        qs = super(BlogsList, self).get_queryset()
        if self.sortform.is_valid():
            qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__contains=self.sortform.cleaned_data['search'])
        return qs


class PostsList(ListView):

    queryset = Post.objects.order_by('-time').all()
    template_name = 'posts/posts.html'
    sortform = None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(PostsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostsList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context

    def get_queryset(self):
        qs = super(PostsList, self).get_queryset()
        if self.sortform.is_valid():
            qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__contains=self.sortform.cleaned_data['search'])
        return qs

class BlogPage(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'


class PostComments(DetailView):

    queryset = Post.objects.order_by('-time').all()
    template_name = 'posts/PostComments.html'


#def show_blog(request, blog_id=None):
  #  blog = Blog.objects.get(id=blog_id)
  #  return render(request, "posts/blog.html", {'blog': blog})
