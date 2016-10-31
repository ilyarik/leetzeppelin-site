from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.conf import settings
from django import forms
from .models import *
from django.db import models
from tinymce.widgets import TinyMCE

class NewsForm(forms.ModelForm):
	text_body = forms.CharField(widget=TinyMCE(mce_attrs={'width':'80%'}), label='Post')
	posted_by = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=True))
	class Meta:
		model = Post
		fields = ['title','image']
		labels = {
			'title' : 'Title your post',
			'image' : 'You can attach the image',
			'posted_by' : 'Posted by',
		}
	class Media:
		js = (
				settings.STATIC_URL + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
				settings.STATIC_URL + 'grappelli/tinymce_setup/tinymce_setup.js',
			)

class NewsAdmin(admin.ModelAdmin):
	form = NewsForm
	
admin.site.register(Post, NewsAdmin)
admin.site.register(PostComment)