# -*- coding: utf-8 -*-
from django import forms
from .models import Blog, Post


class SortForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('title', u'Заголовок'),
        ('-time', u'Время'),
        ('id', u'Id')
    ))
    search = forms.CharField(required=False)


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'description')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'blog')
