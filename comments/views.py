from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Comment
from django.core.urlresolvers import reverse


class CreateComment(UpdateView):
    template_name = "comments/addcomment.html"
    model = Comment
    fields = ('body',)
    success_url = '/blogs/posts/list/'

    def get_queryset(self):
        return super(CreateComment, self).get_queryset().filter(author=self.request.user, post=self.request.GET.get('pk'))