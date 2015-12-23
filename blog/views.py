from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import *

def index(request):
	post_list = Post.objects.order_by('date_time').reverse()
	context = {'post_list':post_list}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404("Post does not exist")
	return HttpResponse("You are viewing post %s" % post_id) 