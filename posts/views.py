from rest_framework import permissions
from django.db.models import Count
from rest_framework import generics, filters

from .models import Post
from .serializers import PostSerializer
from fixit_drf_api.permissions import IsPostCommentOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    List all profiles and create them if authenticated.
    """
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        upvotes_count=Count('post_upvotes', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'comments_count',
        'upvotes_count',
        'post_upvotes__created_at'
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update own, delete own posts for
    authenticated users.
    """
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        upvotes_count=Count('post_upvotes', distinct=True)
    ).order_by('-created_at')
    permission_classes = [IsPostCommentOwnerOrReadOnly]
    serializer_class = PostSerializer
