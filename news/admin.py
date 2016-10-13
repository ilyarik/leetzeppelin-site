from django.contrib import admin
from django.conf import settings
from django import forms
from .models import *
from django.db import models
from tinymce.widgets import TinyMCE

class NewsForm(forms.ModelForm):
	text_body = forms.CharField(widget=TinyMCE(mce_attrs={'width':'80%'}))
	class Meta:
		model = Post
		fields = ['title','image','text_body']
		labels = {
			'title' : 'Title your post',
			'image' : 'You can attach the image',
			'text_body' : 'Post',
		}
	class Media:
		js = (
				settings.STATIC_URL + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
				settings.STATIC_URL + 'grappelli/tinymce_setup/tinymce_setup.js',
			)

class NewsAdmin(admin.ModelAdmin):
	form = NewsForm
	def save_model(self, request, obj, form, change):
		if getattr(obj, 'posted_by', None) is None:
			obj.posted_by = UserProfile.objects.filter(username=request.user.username)[0]
			obj.save()

admin.site.register(Post,NewsAdmin)
admin.site.register(PostComment)