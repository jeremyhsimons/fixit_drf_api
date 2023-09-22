# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from django.db import models
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from comments.models import Comment


class CommentUpvote(models.Model):
    """
    A class for users's upvotes for comments.
    It contains both the user and relevant comment as foreign keys.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='comment_upvotes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'comment']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s upvote for {self.comment.author}'s comment"
