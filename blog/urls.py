from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<post_id>[0-9]+)/add_comment/$', views.addComment, name='add_comment')
]