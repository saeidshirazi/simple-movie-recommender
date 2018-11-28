from django.conf.urls import url
from . import views
from django.contrib import *

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login_user, name='login'),
	url(r'^logout/$', views.logout_user, name='logout'),
	url(r'^register/$', views.reg_user, name='register'),
	url(r'^search/$', views.search, name='search'),
	url(r'^main/$', views.main, name='main'),
	url(r'^movie/(?P<query>\w+)/$', views.movie, name='movie'),
	url(r'^movie/(?P<query>[0-9]{6})/$', views.movie, name='movie'),
]