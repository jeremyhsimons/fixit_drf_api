from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    CHOICES = (
        ('BC', 'Bikes and Cars'),
        ('EC', 'Electronics'),
        ('DIY', 'DIY'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', default="../default_profile_uk3zc1"
    )
    upvotes_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=300, choices=Choices)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author}'s post"
