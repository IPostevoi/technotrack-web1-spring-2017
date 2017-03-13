from django.conf.urls import url, include
from posts.views import BlogsList, PostsList, BlogPage, PostComments


urlpatterns = [
    url(r'^list/$', BlogsList.as_view(), name="blogs"),
    url(r'^posts/list/$', PostsList.as_view(), name="posts"),
    url(r'^posts/post/(?P<pk>\d+)/$', PostComments.as_view(), name="PostComments"),
    url(r'^blog/(?P<pk>\d+)/$', BlogPage.as_view(), name="blog"),

]