#-*- coding: utf8 -*-
from django import forms
from .models import *
from django_countries.widgets import CountrySelectWidget
from tinymce.widgets import TinyMCE
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime

class CommentForm(forms.ModelForm):
	class Meta:
		model = PostComment
		fields = ['text_body']
		widgets = {
			'text_body': forms.Textarea(attrs={'placeholder': 'Send your comment', 'style':'resize:none;'}),
		}
		labels = {
			'text_body': '',
		}

class UserRegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = UserCreationForm.Meta.fields + ('email',)

class UserLoginForm(AuthenticationForm):
	class Meta:
		model = User

class UserProfileChangeForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['avatar','birthday','about','gender','country']
		widgets = {
			'birthday': forms.SelectDateWidget(years=range(1900,datetime.date.today().year)),
			'about': forms.Textarea(attrs={'rows':3,'style':'resize:vertical'}),
			'country': CountrySelectWidget()
		}
