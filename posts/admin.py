from django.contrib import admin
from .models import Blog, Post, Like, Category


# Register your models here.
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Category)