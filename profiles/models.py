# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A class to represent profile data.
    """
    CHOICES = (
        ('LFH', 'Looking for help'),
        ('SME', 'Subject matter expert'),
        ('JB', 'Just browsing'),
        ('AME', 'Ask me anything'),
        ('NA', 'Not active')
    )

    profile_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default="../default_profile_uk3zc1"
    )
    status = models.CharField(max_length=300, choices=CHOICES)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.profile_owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(profile_owner=instance)


post_save.connect(create_profile, sender=User)
