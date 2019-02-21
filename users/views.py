from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages # Types of messages include debug,info,succes,warning and error
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #this is actually wanting to submit info
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm() #this is just a plain ol' get request
    return render(request, 'users/register.html',{'form': form})

