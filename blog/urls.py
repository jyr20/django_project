from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    # empty path with function 'home' defined in ./views.py, the http reponse
    # that we are on blog page, name this path
    path('', PostListView.as_view(), name='blog-home'), 
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'), 
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete'),
    #template is NOT what you expect: it shares one with update
    path('post/new/',PostCreateView.as_view(), name='post-create'), 
    path('about/', views.about, name='blog-about'),
]
