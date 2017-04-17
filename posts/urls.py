from django.conf.urls import url, include
from django.contrib.auth.decorators import  login_required
from posts.views import BlogsList, PostsList, BlogPage, PostComments, CommentsList
from posts.views import CreateBlog, UpdateBlog, CreatePost, UpdatePost, BlogLikeAjaxView
from comments.views import CreateComment

urlpatterns = [
    url(r'^list/$', BlogsList.as_view(), name="blogs"),
    url(r'^posts/list/$', PostsList.as_view(), name="posts"),
    url(r'^posts/post/(?P<pk>\d+)/$', PostComments.as_view(), name="post"),
    url(r'^blog/(?P<pk>\d+)/$', BlogPage.as_view(), name="blog"),
    url(r'^new/$', login_required(CreateBlog.as_view()), name="add_blog"),
    url(r'^blog/(?P<pk>\d+)/edit/$', login_required(UpdateBlog.as_view()), name="edit_blog"),
    url(r'^blog/(?P<pk>\d+)/addpost', login_required(CreatePost.as_view()), name="add_post"),
    url(r'^posts/post/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="edit_post"),
    url(r'^posts/post/(?P<pk>\d+)/addcomment/$', login_required(CreateComment.as_view()), name="add_comment"),
    url(r'^blog/(?P<pk>\d+)/blog_ajax_like/$', login_required(BlogLikeAjaxView.as_view()), name="blog_ajax_like"),
    url(r'^posts/post/(?P<pk>\d+)/comments$', CommentsList.as_view(), name="post_comments"),



]