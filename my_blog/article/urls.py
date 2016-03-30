from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^index/$',views.index,name='index'),
	url(r'^login/$',views.login,name='login'),
	url(r'^signup/$',views.signup,name='signup'),
	#url(r'^search/$',views.search,name='search'),
	#url(r'^search_return/$',views.search_return,name='searchreturn'),
	#url(r'^(?P<myargv>\d+)/$', views.detail,name = 'detail')
]