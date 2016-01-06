from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import *

siteTitle = "Michael J. Irvine"
page_list = StaticPage.objects.order_by('title')

def index(request):
	post_list = Post.objects.order_by('date_time').reverse()
	context = {'post_list':post_list, 'menu':page_list, 'site_title':siteTitle}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404("Post does not exist")
	try: 
		post_next = post.get_next_by_date_time()
	except Post.DoesNotExist:
		post_next = None
	try:
		post_prev = post.get_previous_by_date_time()
	except Post.DoesNotExist:
		post_prev = None
	context = {'site_title':siteTitle, 'menu':page_list, 'post':post,
		'next':post_next, 'prev':post_prev}
	return render(request, 'blog/post.html', context)

def static(request, page_id):
	try:
		page = StaticPage.objects.get(pk=page_id)
	except StaticPage.DoesNotExist:
		raise Http404("Page does not exist")
	context = {'site_title':siteTitle, 'menu':page_list, 'page':page}
	return render(request, 'blog/static.html', context)