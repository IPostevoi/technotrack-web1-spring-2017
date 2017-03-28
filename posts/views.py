# -*- coding: utf-8 -*-
from .models import Blog, Post
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django import forms
from django.core.urlresolvers import reverse
from posts.forms import SortForm


class UpdateBlog(UpdateView):

    template_name = "posts/edit_blog.html"
    model = Blog
    fields = ('title', 'description', 'pic')

    def get_success_url(self):
        return reverse('posts:blogs')

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)

    def form_valid(self, form):
        return super(UpdateBlog, self).form_valid(form)


class CreateBlog(CreateView):

    template_name = "posts/add_blog.html"
    model = Blog
    fields = ('title', 'description', 'pic')

    def get_success_url(self):
        return reverse('posts:blogs')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBlog, self).form_valid(form)


class UpdatePost(UpdateView):
    template_name = "posts/edit_post.html"
    model = Post
    fields = ('title', 'text', 'blog')

    def get_success_url(self):
        return reverse('posts:posts')

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)


class CreatePost(CreateView):
    template_name = "posts/add_post.html"
    model = Post
    fields = ('title', 'text')

    def get_success_url(self):
        return reverse('posts:blog', args=(self.object.blog_id,))

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = Blog.objects.get(id=self.kwargs['pk'])
        return super(CreatePost, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(CreatePost, self).get_form()
        #form.fields["blog"].queryset = Blog.objects.filter(author=self.request.user)
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
            if self.sortform.cleaned_data['sort'] == 'author':
                qs = qs.filter(author_id=self.request.user)
            else:
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
            if self.sortform.cleaned_data['sort'] == 'author':
                qs = qs.filter(author_id=self.request.user)
            else:
                qs = qs.order_by(self.sortform.cleaned_data['sort'])
        if self.sortform.cleaned_data['search']:
            qs = qs.filter(title__contains=self.sortform.cleaned_data['search'])
        return qs


class BlogPage(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'


class PostComments(DetailView):

    queryset = Post.objects.order_by('-time').all()
    template_name = 'posts/post_comments.html'


