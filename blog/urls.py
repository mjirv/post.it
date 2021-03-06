from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/(?P<post_id>[0-9]+)$', views.detail, name='detail'),
	url(r'^static/(?P<page_id>[0-9]+)$', views.static, name='static')
]
