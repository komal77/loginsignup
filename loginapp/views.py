# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm

class Home(View):
	def get(self, request, *args, **kwargs):
		return render(request, "home.html")

class Login(View):
	def get(self, request, *args, **kwargs):
		form = UserLoginForm(request.POST or None)
		context = {
		'form': form,
		}
		return render(request, "login.html", context)
		
	def post(self, request, *args, **kwargs):
	    next = request.GET.get('next')
	    form = UserLoginForm(request.POST or None)
	    if form.is_valid():
	        username = form.cleaned_data.get('username')
	        password = form.cleaned_data.get('password')
	        user = authenticate(username=username, password=password)
	        login(request, user)
	        if next:
	            return redirect(next)
	        return redirect('/loginapp')
	    else:
	    	context = {'message': "login credentials are incorrect"}
	    	return render(request, "login.html", context)

	    # context = {
	    #     'form': form,
	    # }
	    # return render(request, "login.html", context)

class Signup(View):
	def get(self, request, *args, **kwargs):
		form = UserRegisterForm(request.POST or None)
		context = {
		'form': form,
		}
		return render(request, "signup.html", context)

	def post(self, request, *args, **kwargs):
	    next = request.GET.get('next')
	    form = UserRegisterForm(request.POST or None)
	    if form.is_valid():
	        user = form.save(commit=False)
	        password = form.cleaned_data.get('password')
	        user.set_password(password)
	        user.save()
	        new_user = authenticate(username=user.username, password=password)
	        login(request, new_user)
	        if next:
	            return redirect(next)
	        return redirect('/loginapp/login')
	    else:
	    	context = {'message': "error"}
	    	return render(request, "signup.html", context)

	    

class Logout(View):
	def post(self, request, *args, **kwargs):
	    logout(request)
	    return redirect('/')