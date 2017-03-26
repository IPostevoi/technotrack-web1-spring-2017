# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Blog, Post
#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django import forms

class SortForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('title', u'Заголовок'),
        ('-time', u'Время'),
        ('id', u'Id')
    ))
    search = forms.CharField(required=False)


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
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs


class PostsList(ListView):

    queryset = Post.objects.order_by('-time').all()
    template_name = 'posts/posts.html'


class BlogPage(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'


class PostComments(DetailView):

    queryset = Post.objects.order_by('-time').all()
    template_name = 'posts/PostComments.html'


#def show_blog(request, blog_id=None):
  #  blog = Blog.objects.get(id=blog_id)
  #  return render(request, "posts/blog.html", {'blog': blog})
