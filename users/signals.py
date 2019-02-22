from django.db.models.signals import post_save
# User will send the signal
from django.contrib.auth.models import User
# Receiver will receive the signal
from django.dispatch import receiver
# Need access to Profile class
from .models import Profile

# When a user is saved, send this signal, which is received by the create_profile function,
# which takes all signals post_save gave it as arguments: instance, created
# If user was created, make an associated profile
@receiver(post_save, sender=User) #post_save is the signal
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User) #post_save is the signal
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
