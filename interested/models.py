from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Interested(models.Model):
    """
    Represents a user's interest in an event.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name='interested', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'event']

    def __str__(self):
        return f'{self.owner} is interested in {self.event}'
