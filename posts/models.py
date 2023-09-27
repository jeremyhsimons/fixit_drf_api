# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    A class to represent post data in the database.
    """
    CHOICES = (
        ('BC', 'Bikes and Cars'),
        ('EC', 'Electronics'),
        ('DIY', 'DIY'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="Title")
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=300, choices=CHOICES)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author}'s post"
