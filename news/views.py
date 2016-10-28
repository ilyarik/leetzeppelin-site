#-*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, redirect, HttpResponse, Http404, get_object_or_404, get_list_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from .forms import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.conf import settings

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
	return render(request, 'news/home.html', {
		'posts' : posts,
		'current_date' : current_date,
		'current_user': current_user,
		})

def post(request, id):
	post = get_object_or_404(Post, id=id)
	comments = PostComment.objects.filter(post=id)
	current_user = request.user
	if request.method == 'POST':
		add_comment = CommentForm(request.POST)
		if add_comment.is_valid():
			comment = PostComment()
			comment.posted_by = UserProfile.objects.filter(username=current_user)[0]
			comment.post = Post.objects.get(id=id)
			comment.text_body = u'%s'%(request.POST["text_body"])
			comment.time_post = datetime.datetime.now()
			comment.save()
			post.num_of_comments+=1
			post.save()
			return redirect(request.META['HTTP_REFERER'])
		try:
			del_comment_id = request.POST['del_comment']
			comment = get_object_or_404(PostComment, id=del_comment_id)
			if comment.posted_by.id == current_user.id:
				post.num_of_comments-=1
				post.save()
				comment.delete()
		except:
			pass
	
	return render(request, 'news/post.html', {
		'post' : post,
		'current_date' : current_date,
		'form' : CommentForm,
		'comments' : comments,
		'current_user' : current_user,
		})

def register(request):
	new_user = UserProfile()
	if request.method == 'POST':
		if UserProfile.objects.filter(username=request.POST['username']):
			raise Http404("User already exist")
		else:
			new_user.username = request.POST['username']

		new_user.password = make_password(request.POST['password'])
		
		if UserProfile.objects.filter(email=request.POST['email']):
			raise Http404("Email already registered")
		else:
			new_user.email = request.POST['email']

		new_user.save()
		return redirect("/")

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
	          	raise Http404("Inactive user")  
	    else:
	        raise Http404("Incorrect data")
	else:
		return render(request, 'news/login.html', {
			'loginForm' : UserLoginForm,
			})

def signOut(request):
	if request.user.is_authenticated:
		logout(request)
	return redirect("/")

def profile(request, user):
	user = get_list_or_404(UserProfile, username=user)[0] #user who page we see
	current_user = request.user 						#user who logged
	if request.method == 'POST' and current_user.id == user.id:
		userProfileForm = UserProfileChangeForm(request.POST)
		if userProfileForm.is_valid():
			try:
				user.avatar = request.FILES['avatar']
			except:
				pass

			if request.POST['country']:
				user.country = request.POST['country']
			else:
				user.country = None

			if request.POST['gender']:
				user.gender = request.POST['gender']

			if request.POST['birthday']:
				user.birthday = request.POST['birthday']
			else:
				user.birthday = None

			if request.POST['about']:
				user.about = request.POST['about']
			else: 
				user.about = None
				
			user.save()
			return redirect(request.META['HTTP_REFERER'])

	if user.birthday:
		birthday = user.birthday.strftime('%Y-%m-%d') 
	else:
		birthday = None

	return render(request, 'news/profile.html', {
		'user' : user,
		'current_user' : current_user,
		'current_date' : current_date,
		'UserProfileChangeForm' : UserProfileChangeForm({
			'country' : user.country,
			'gender' : user.gender,
			'birthday' : birthday,
			'about' : user.about,
			}),
		})
