from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^dbgui$', views.dbgui),
	url(r'^hot$', views.hot),
	url(r'^courses/create$', views.courses_create),
	url(r'^courses/delete/(?P<id>\d+)$', views.courses_delete),
]