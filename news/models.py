#-*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=80)
	text_body = models.TextField()
	time_post = models.DateTimeField(auto_now=False)
	image = models.ImageField(upload_to='news', null=True, blank=True)

	class Meta:
		verbose_name = u"Post"
		verbose_name_plural = u"Posts"

	def __str__(self):
		return self.title

class PostComment(models.Model):
	author = models.CharField(max_length=80)
	post_fk = models.ForeignKey(
		'Post',
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		)
	text_body = models.TextField()
	time_post = models.DateTimeField(auto_now=False)

	def __str__(self):
		return self.author

class UserProfile(User):
    class Meta:
    	verbose_name = u"User"
    	verbose_name_plural = u"Users"