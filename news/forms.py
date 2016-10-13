#-*- coding: utf8 -*-
from django import forms
from .models import *
from django_countries.widgets import CountrySelectWidget
from tinymce.widgets import TinyMCE

class CommentForm(forms.Form):
	text_body = forms.CharField(
		label="", widget=forms.Textarea(attrs={'placeholder': 'Send your comment'})
		)
	class Meta:
		model = PostComment

class UserRegisterForm(forms.Form):
	username = forms.CharField(label="Username: ")
	password = forms.CharField(label="Password: ", widget=forms.PasswordInput)
	email = forms.EmailField(label="Email", widget=forms.EmailInput)
	class Meta:
		model = UserProfile

class UserLoginForm(forms.Form):
	username = forms.CharField(label="Username: ")
	password = forms.CharField(label="Password: ", widget=forms.PasswordInput)
	class Meta:
		model = UserProfile

class UserProfileChangeForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['avatar','birthday','about','gender','country']
		widgets = {
            'birthday': forms.DateInput(),
            'about': forms.Textarea(),
            'country': CountrySelectWidget()
        }