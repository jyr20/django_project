from django.shortcuts import render
from django.http import HttpResponse

#This is where the logic goes for how we want to handle certain routes

def home(request):
    '''Return a http response that says we're on the home page'''
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
