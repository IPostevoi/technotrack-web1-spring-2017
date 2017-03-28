from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Comment
from posts.models import Post
from django.core.urlresolvers import reverse


class CreateComment(CreateView):

    template_name = "comments/add_comment.html"
    model = Comment
    fields = ('body',)

    def get_success_url(self):
        return reverse('posts:post_comments', args=(self.object.post_id,))

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super(CreateComment, self).form_valid(form)


