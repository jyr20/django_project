#This is where the logic goes for how we want to handle certain routes

from django.shortcuts import render
from .models import Post


def home(request):
    """ Returns a HTTP request or exception"""
    # Define this dictionary key to above fake data so that in home.html 
    # we can refer to the above dictionary as 'posts'
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
