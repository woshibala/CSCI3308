from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^index/$',views.index,name='index'),
	url(r'^login/$',views.login,name='login'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^signup_return/$',views.signup_return,name='signupreturn'),
	url(r'^login_return/$',views.login_return,name='login_return'),
	url(r'^add/$',views.add,name='add'),
	url(r'^add_return/$',views.add_return,name='add_return'),

]