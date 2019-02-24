#This is where the logic goes for how we want to handle certain routes

from django.shortcuts import render, get_object_or_404
#like a function decorator but for class via inheritence
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    """ Returns a HTTP request or exception"""
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #by default looks for app/model_type.html, e.g. blog/post_list.html
    context_object_name = 'posts' #the name to be referenced in template, by default it sends object_list
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #by default looks for app/model_type.html, e.g. blog/post_list.html
    context_object_name = 'posts' #the name to be referenced in template, by default it sends object_list
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    # by default will look for template/blog/post_detail.html and can reference context as 'object' in template
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): #inherit LoginRequiredMixin first
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #override form_valid method
        #before submitting form, set author to user
        form.instance.author = self.request.user
        return super().form_valid(form) #run what was going to be run anyway

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView): #inherit LoginRequiredMixin first
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #override form_valid method
        #before submitting form, set author to user
        form.instance.author = self.request.user
        return super().form_valid(form) #run what was going to be run anyway

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # by default will look for template/blog/post_detail.html and can reference context as 'object' in template
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
