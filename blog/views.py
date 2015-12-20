from django.http import HttpResponse

def index(request):
	return HttpResponse("Woo at the blog index.")

def addComment(request, post_id):
	return HttpResponse("You are adding a comment to post %s" % post_id) 