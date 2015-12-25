from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import *

siteTitle = "Michael J. Irvine"

def index(request):
	post_list = Post.objects.order_by('date_time').reverse()
	page_list = StaticPage.objects.order_by('title')
	context = {'post_list':post_list, 'menu':page_list, 'site_title':siteTitle}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404("Post does not exist")
	return HttpResponse("You are viewing post %s" % post_id) 

def static(request, page_id):
	try:
		page = StaticPage.objects.get(pk=page_id)
	except StaticPage.DoesNotExist:
		raise Http404("Page does not exist")
	page_list = StaticPage.objects.order_by('title')
	context = {'site_title':siteTitle, 'menu':page_list, 'page':page}
	return render(request, 'blog/static.html', context)