#-*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Post(models.Model):
	title = models.CharField(max_length=80)
	text_body = models.TextField()
	time_post = models.DateTimeField(auto_now=False, auto_now_add=True)
	image = models.ImageField(upload_to='news', null=True, blank=True)
	posted_by = models.ForeignKey(
		to=User,
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		)
	num_of_comments = models.IntegerField(default=0)

	class Meta:
		verbose_name = u"Post"
		verbose_name_plural = u"Posts"

	def __str__(self):
		return self.title

class PostComment(models.Model):
	post = models.ForeignKey(
		to=Post,
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		)
	posted_by = models.ForeignKey(
		to=User,
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		)
	text_body = models.TextField()
	time_post = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.post.title+" : "+self.posted_by.username+" : "+self.text_body


class UserProfile(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
	gender = models.CharField(default='M', max_length=1, choices=GENDER_CHOICES)
	birthday = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	avatar = models.ImageField(upload_to="news", null=True, blank=True, default=None)
	about = models.TextField(null=True, blank=True)
	country = CountryField(null=True, blank=True, blank_label='(select country)')

	class Meta:
		verbose_name = u"User"
		verbose_name_plural = u"Users"

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_userprofile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_userprofile(sender, instance, **kwargs):
	instance.userprofile.save()
