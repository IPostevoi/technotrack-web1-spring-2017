# -*- coding: utf-8 -*-
from .models import Blog, Post, Category, Like
from comments.models import Comment
from core.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django import forms
from django.core.urlresolvers import reverse
from posts.forms import SortForm
from crispy_forms.helper import FormHelper
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from crispy_forms.bootstrap import Field
from crispy_forms.layout import Submit, Layout, Fieldset


class UpdateBlog(UpdateView):

    template_name = "posts/edit_blog.html"
    model = Blog
    fields = ('title', 'description', 'pic')

    def get_success_url(self):
        return reverse('posts:blogs')

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)

    def form_valid(self, form):
        response = super(UpdateBlog, self).form_valid(form)
        return HttpResponse('OK')
        #return super(UpdateBlog, self).form_valid(form)

    # def post(self, request):
    #     return HttpResponse('valid')


class CreateBlog(CreateView):

    template_name = "posts/add_blog.html"
    model = Blog
    fields = ('title', 'description', 'pic')

    def get_success_url(self):
        return reverse('posts:blogs')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBlog, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(CreateBlog, self).get_form()
        # form.fields["blog"].queryset = Blog.objects.filter(author=self.request.user)
        return form


    # model = Blog
    # fields = ('title', 'description', 'pic')
    # create_form = None
    #
    # def dispatch(self, request, *args, **kwargs):
    #     self.create_form = CreateBlogForm()
    #     return super(CreateBlog, self).dispatch(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(CreateBlog, self).get_context_data(**kwargs)
    #     context['create_form'] = self.create_form
    #     return context
    #
    # def get_queryset(self):
    #     return super(CreateBlog, self).get_queryset()


    # template_name = "posts/add_blog.html"
    # model = Blog
    # fields = ('title', 'description', 'pic')
    #
    # def get_form(self, form_class=None):
    #     form = super(CreateBlog, self).get_form(form_class)
    #     form.helper = FormHelper()
    #     form.helper.add_input(Submit('submit', 'Отправить', css_class='btn-primary'))
    #     return form


class UpdatePost(UpdateView):

    template_name = "posts/edit_post.html"
    model = Post
    fields = ('title', 'text')

    def get_success_url(self):
        return reverse('posts:post', args=(self.object.id,))

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = Blog.objects.get(id=self.kwargs['pk'])
        return super(UpdatePost, self).form_valid(form)
        #response  =super(UpdatePost, self).form_valid(form)
        #return HttpResponse('valid')

    def post(self, request):
        return HttpResponse('valid')


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
    recent_posts = Post.objects.order_by('-time')[:5][::-1]
    categories = Category.objects.all()

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        context['recent_posts'] = self.recent_posts
        context['categories'] = self.categories
        return context

    def get_queryset(self):
        qs = super(BlogsList, self).get_queryset()
        sort = self.request.GET.get('user')
        category = self.request.GET.get('category')
        if sort:
            user = User.objects.filter(username=sort)
            qs = qs.filter(author=user)

        if category:
            qs = qs.filter(category__id=category)

        # if self.searchform.is_valid():
        #
        #     # else:
        #     #     qs = qs.order_by(self.sortform.cleaned_data['sort'])
        #     if self.searchform.cleaned_data['search']:
        #         qs = qs.filter(title__contains=self.searchform.cleaned_data['search'])
        if self.sortform.is_valid():
            qs = qs.order_by(self.sortform.cleaned_data['sort'])
        return qs


class PostsList(ListView):

    queryset = Post.objects.order_by('-time').all()
    template_name = 'posts/posts.html'
    # sortform = None
    #
    # def dispatch(self, request, *args, **kwargs):
    #     self.sortform = SortForm(self.request.GET)
    #     return super(PostsList, self).dispatch(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(PostsList, self).get_context_data(**kwargs)
    #     context['sortform'] = self.sortform
    #     return context
    #
    # def get_queryset(self):
    #     qs = super(PostsList, self).get_queryset()
    #     if self.sortform.is_valid():
    #         if self.sortform.cleaned_data['sort'] == 'author':
    #             qs = qs.filter(author_id=self.request.user)
    #         else:
    #             qs = qs.order_by(self.sortform.cleaned_data['sort'])
    #     if self.sortform.cleaned_data['search']:
    #         qs = qs.filter(title__contains=self.sortform.cleaned_data['search'])
    #     return qs


class BlogPage(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'


class PostComments(DetailView):

    queryset = Post.objects.all()
    template_name = 'posts/post.html'


class BlogLikeAjaxView(View):

    blog_object = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        # Забираем из базы пост, который собираются лайкнуть
        self.blog_object = get_object_or_404(Blog, id=pk)
        return super(BlogLikeAjaxView, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        if not self.blog_object.like_set.filter(author=self.request.user).exists():
            # Сначала мы проверили, что лайка от этого юзера у поста еще нет
            # Теперь мы здесь должны создать лайк, и вернуть новое количество лайков у поста
            like = Like(blog=self.blog_object, author=self.request.user)
            like.save(force_insert=True)

        return HttpResponse(Like.objects.filter(blog=self.blog_object).count())


class CommentsList(ListView):

    template_name = 'posts/comments.html'
    queryset = Comment.objects.all()

    def get_queryset(self):
        return super(CommentsList, self).get_queryset().filter(post_id=self.kwargs['pk'])



