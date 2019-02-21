#This is where the logic goes for how we want to handle certain routes

from django.shortcuts import render

#fake date for now
posts = [
    {
        'author': 'ReinessJ',
        'title': 'My first blog post',
        'content': 'First content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'DoeJ',
        'title': 'OMG!',
        'content': 'Second content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    """ Returns a HTTP request or exception"""
    # Define this dictionary key to above fake data so that in home.html 
    # we can refer to the above dictionary as 'posts'
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
