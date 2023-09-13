from django.db import models
from django.contrib.auth.models import User

from posts.models import Post


class PostUpvote(models.Model):
    """
    A class for users bookmarks to save a post
    for later viewing. It contains both the user
    and relevant post as foreign keys.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_upvotes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'post']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s upvote for {self.post.author}'s post"
