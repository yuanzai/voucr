from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
            if form.is_valid():
                # Do something with the data
                pass
    else:
        form = UserCreationForm()
        return render(request, 'template/signup.html',{'form':form})
