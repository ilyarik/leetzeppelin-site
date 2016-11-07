#-*- coding: utf8 -*-
from django import forms
from .models import *
from django_countries.widgets import CountrySelectWidget
from tinymce.widgets import TinyMCE

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

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password','email']
		widgets = {
			'password': forms.PasswordInput,
			'email': forms.EmailInput,
		}

class UserLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']
		widgets = {
			'password': forms.PasswordInput,
		}

class UserProfileChangeForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['avatar','birthday','about','gender','country']
		widgets = {
            'birthday': forms.DateInput(attrs={'title' : 'Input birth date in "YYYY-MM-dd" format.'}),
            'about': forms.Textarea(attrs={'rows':3,'style':'resize:vertical'}),
            'country': CountrySelectWidget()
        }
