from posts.models import Blog, Post
from comments.models import Comment
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "core/home_page.html"

    def get_context_data(self, **kwargs):

        context = super(HomePageView, self).get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all().count()
        context["posts"] = Post.objects.all().count()
        context["comments"] = Comment.objects.all().count()
        return context


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class RegisterFormView(CreateView):

    form_class = CustomUserCreationForm
    success_url = 'login'
    template_name = 'core/register.html'

    def get_success_url(self):
        return reverse('core:login')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

