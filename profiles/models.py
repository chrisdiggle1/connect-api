from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Extends the default User model by storing additional information
    about the user. The profile is automatically created and linked
    when a User instance is saved for the first time.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True)
    profile_picture = models.ImageField(
        upload_to='images/', default='../default_profile_st6mnc'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
