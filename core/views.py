from posts.models import Blog, Post
from comments.models import Comment

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "core/startPage.html"

    def get_context_data(self, **kwargs):
        
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all().count()
        context["posts"] = Post.objects.all().count()
        context["comments"] = Comment.objects.all().count()
        return context

