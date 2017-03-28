from django.conf.urls import url
from django.contrib.auth.views import login, logout
from core.views import RegisterFormView

urlpatterns = [
    url(r'^login/$', login, {"template_name": 'core/login.html'}, name='login'),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', RegisterFormView.as_view(), name='register')
]