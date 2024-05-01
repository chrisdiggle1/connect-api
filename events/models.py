from django.db import models
from django.contrib.auth.models import User

EVENT_CATEGORIES = (
    ("Health and Wellness", "Health and Wellness"),
    ("Sport", "Sport"),
    ("Music", "Music"),
    ("Technology", "Technology"),
    ("Family", "Family"),
    ("Kids", "Kids"),
    ("Food and Drink", "Food and Drink"),
    ("Arts and Crafts", "Arts and Crafts"),
    ("Education", "Education"),
)


class Event(models.Model):
    """
    This is the model for events created by a user. Events can be
    categorised into various types such as Sport, Music, technology,
    etc. Each event contains details about the event, such as title,
    time, an image and description.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_event_fqptco', blank=True
    )
    event_date = models.DateField(blank=True)
    category = models.CharField(
        max_length=50, choices=EVENT_CATEGORIES, default='Sport'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'