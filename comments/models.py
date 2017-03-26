from __future__ import unicode_literals
from django.conf import settings
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')
    post = models.ForeignKey('posts.Post')
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
