"""
Views to handle logic of sending/receiving comment data
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from fixit_drf_api.permissions import IsPostCommentOwnerOrReadOnly


class CommentList(generics.ListCreateAPIView):
    """
    Retrieve a list, create a comment if authenticated.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.annotate(
        upvotes_count=Count('comment_upvotes', distinct=True)
    ).order_by('created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'post',
    ]
    ordering_fields = [
        'upvotes_count',
        'comment_upvotes',
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a single comment, update comment, delete comment.
    For authenticated user.
    """
    permission_classes = [IsPostCommentOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        upvotes_count=Count('comment_upvotes', distinct=True)
    ).order_by('created_at')
