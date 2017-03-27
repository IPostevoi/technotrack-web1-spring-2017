from django.conf.urls import url, include
from django.contrib.auth.decorators import  login_required
from posts.views import BlogsList, PostsList, BlogPage, PostComments, CreateBlog, UpdateBlog, CreatePost, UpdatePost
from comments.views import CreateComment

urlpatterns = [
    url(r'^list/$', BlogsList.as_view(), name="blogs"),
    url(r'^posts/list/$', PostsList.as_view(), name="posts"),
    url(r'^posts/post/(?P<pk>\d+)/$', PostComments.as_view(), name="PostComments"),
    url(r'^blog/(?P<pk>\d+)/$', BlogPage.as_view(), name="blog"),
    url(r'^new/$', login_required(CreateBlog.as_view()), name="addblog"),
    url(r'^blog/(?P<pk>\d+)/edit/$', login_required(UpdateBlog.as_view()), name="editblog"),
    url(r'^posts/new/$', login_required(CreatePost.as_view()), name="addpost"),
    url(r'^posts/post/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="editpost"),
    url(r'^posts/post/(?P<pk>\d+)/addcomment/$', login_required(CreateComment.as_view()), name="addcomment"),


]