from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.


#class Category(models.Model):

 #   title = models.CharField()
    #blogs = models.ManyToManyField(Blog)


#class Like(models.Model):
    #post = models.ForeignKey(Post)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='liked_posts')


class Blog(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='published_blogs')
    time = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to='blog_pic', blank=True, null=True)
    #categories = models.ForeignKey(Category)
    

class Post(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    blog = models.ForeignKey('posts.Blog')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='published_posts')
    time = models.DateTimeField(auto_now_add=True)
