from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404

import sys

def index(request):
    if not request.user.is_authenticated():
        return HttpResponse('Error')
    else:
    	return HttpResponse(request.user.Username)

def logout(request):
    logout(request)
    return HttpResponse('Logged out')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
            else:
                pass
                # Return a 'disabled account' error message
        else:
            # Return an 'invalid login' error message.

            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return HttpResponseRedirect(reverse('index'))
    else:
    	form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
	    username = form.clean_username()
            password = form.clean_password2()
            form.save()
	    form = authenticate(username=username,
                                password=password)
            login(request, form)
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            #return HttpResponse('Sign Up Success')
        #else:
            #return HttpResponse('Sign Up Failed')
        return render(request, 'signup.html',{'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html',{'form':form})
