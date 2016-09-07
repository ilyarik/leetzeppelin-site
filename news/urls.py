from django.conf.urls import url, include
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    url(r'^(?P<page>\d*)$', views.news, name='home'),
    url(r'^post/(?P<id>\d+)$', views.post, name='post'),
    url(r'^signUp/$', views.register, name='registration'),
    url(r'^signIn/$', views.signIn, name="sign in"),
    url(r'^signOut/$', views.signOut, name="sign out"),
] 