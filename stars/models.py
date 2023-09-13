from django.db import models
from django.contrib.auth.models import User

from profiles.models import Profile


class Star(models.Model):
    """
    A class to handle data for profile 'stars'.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='bookmarks'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'profile']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s star for {self.profile.profile_owner}"
