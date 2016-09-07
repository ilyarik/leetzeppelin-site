#-*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, redirect, HttpResponse
from .models import Post, PostComment, UserProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from .forms import CommentForm, UserRegisterForm, UserLoginForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

current_date = datetime.date.today()

def news(request, page=1):
	post_list = Post.objects.all().order_by('-time_post')
	paginator = Paginator(post_list, 5)
	current_user = request.user
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	return render_to_response('news/home.html', {
		'posts' : posts,
		'current_date' : current_date,
		'current_user': current_user,
		})

def post(request, id):
	post = Post.objects.get(id=id)
	comments = PostComment.objects.filter(post_fk=id)
	current_user = request.user
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = PostComment()
			comment.author = current_user
			comment.post_fk_id = int(id)
			comment.text_body = u'%s'%(request.POST["text_body"])
			comment.time_post = datetime.datetime.now()
			comment.save()
			return redirect(request.META['HTTP_REFERER'])
	else:
		form = CommentForm
	return render(request, 'news/post.html', {
		'post' : post,
		'current_date' : current_date,
		'form' : form,
		'comments' : comments,
		'current_user' : current_user,
		})

def register(request):
	new_user = UserProfile()
	if request.method == 'POST':
	    new_user.username = request.POST['username']
	    new_user.password = make_password(request.POST['password'])
	    new_user.email = request.POST['email']
	    new_user.save()
	    return redirect("/")
	else:
		return render(request, 'news/register.html', {
			'registerForm' : UserRegisterForm,
			})

def signIn(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            return redirect("/")
	        else:
	          	return HttpResponse("<h4>inactive user</h4>")  
	    else:
	        return HttpResponse("<h4>incorrect user</h4>")
	else:
		return render(request, 'news/login.html', {
			'loginForm' : UserLoginForm,
			})

def signOut(request):
	if request.user.is_authenticated:
		logout(request)
	return redirect("/")	