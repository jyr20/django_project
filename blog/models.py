from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here. Models are written as Python classes. 
# Each class will be its own table in the database.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete says what to do if user is deleted - what happens to post?

    def __str__(self):
        return self.title
