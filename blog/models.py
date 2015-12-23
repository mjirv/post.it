from django.db import models
from tinymce.models import HTMLField

class Comment(models.Model):
	date_time = models.DateTimeField('date commented')
	article = models.ForeignKey('Post', on_delete=models.CASCADE)
	author = models.CharField(max_length=100)
	email = models.EmailField()
	content = models.TextField()

	def __str__(self):
		return [self.post, self.author, self.content[:50]]


class Post(models.Model):
	title = models.CharField(max_length=200)
	date_time = models.DateTimeField('date published')
	content = HTMLField()
	comments = models.ManyToManyField('Comment', blank=True)

	def __str__(self):
		return self.title