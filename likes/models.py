from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Like(models.Model):
    """
    Like model, related to 'owner' and 'event'.
    'owner' is a User instance and 'event' is an Event instance.
    'unique_together' ensures a user can't like the same event twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'event']

    def __str__(self):
        return f'{self.owner} {self.event}'
