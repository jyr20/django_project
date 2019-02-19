from django.urls import path
from . import views

urlpatterns = [
    # empty path with function 'home' defined in ./views.py, the http reponse
    # that we are on blog page, name this path
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
