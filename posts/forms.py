# -*- coding: utf-8 -*-
from django import forms
from .models import Blog, Post
from django.core.files.images import get_image_dimensions

class SortForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('title', u'Заголовок'),
        ('-time', u'Время'),
        ('id', u'Id'),
        ('my', u'Мои Блоги'),
    ))
    search = forms.CharField(required=False)


#class BlogForm(forms.ModelForm):
    #class Meta:
       # model = Blog

    #def clean_avatar(self):
       # pic = self.cleaned_data['pic']

        #try:
            #w, h = get_image_dimensions(avatar)

            #validate dimensions
            #max_width = max_height = 100
            #if w > max_width or h > max_height:
                #raise forms.ValidationError(
                   # u'Please use an image that is '
                     #'%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
           # main, sub = avatar.content_type.split('/')
            #if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                #raise forms.ValidationError(u'Please use a JPEG, '
                  #  'GIF or PNG image.')

            #validate file size
            #if len(pic) > (20 * 1024):
                #raise forms.ValidationError(
                  #  u'Avatar file size may not exceed 20k.')

        #except AttributeError:
            #"""
           # Handles case when we are updating the user profile
            #and do not supply a new avatar
            #"""
            #pass

       # return pic


#class BlogForm(forms.ModelForm):

 #   class Meta:
  #      model = Blog
   #     fields = ('title', 'description')


#class PostForm(forms.ModelForm):

 # class Meta:
  #      model = Post
   #     fields = ('title', 'text', 'blog')
