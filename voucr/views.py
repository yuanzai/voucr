from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
	    username = form.clean_username()
            password = form.clean_password2()
            form.save()
            # Do something with the data
            pass
    else:
        form = UserCreationForm()
        return render(request, 'signup.html',{'form':form})
