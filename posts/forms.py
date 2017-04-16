# -*- coding: utf-8 -*-
from django import forms
from .models import Blog, Post
from django.core.files.images import get_image_dimensions
from crispy_forms.helper import FormHelper
from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import Field
from crispy_forms.layout import Submit, Layout, Fieldset
from django.views.generic import ListView, DetailView, CreateView, UpdateView

class SortForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('title', u'Заголовок'),
        ('-time', u'Время'),
    ))


# class CreateBlogForm(CreateView):
#
#     model = Blog
#     fields = ('title', 'description', 'pic')
#
#     def __init__(self):
#         super(CreateBlogForm, self).__init__()
#         self.helper = FormHelper()
#         self.helper.form_show_labels = False
#         self.helper.form_method = 'get'
#         self.helper.form_action = reverse('posts:blogs')
#         self.helper.layout = Layout(
#             Field('title', css_class="col-md-12"),
#             Field('description', css_class="col-md-12"),
#
#         )


# class SearchForm(forms.Form):
#     search = forms.CharField(required=False)

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
