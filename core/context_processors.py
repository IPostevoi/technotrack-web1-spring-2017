from .forms import SearchForm
from posts.models import Blog
import json
from django.core.serializers.json import DjangoJSONEncoder



def search_form(request):
    return {
            'search_form': SearchForm()
           }


def get_blogs(request):
    blogs = Blog.objects.all()
    blogs_list = list(blogs.values('title', 'id'))
    blogs_json = json.dumps(blogs_list)
    return {
            'get_blogs': blogs_json
           }
