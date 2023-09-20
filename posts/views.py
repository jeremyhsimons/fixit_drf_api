from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

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
        comments_count=C
    )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update own, delete own posts for
    authenticated users.
    """
    queryset = Post.objects.all()
    permission_classes = [IsPostCommentOwnerOrReadOnly]
    serializer_class = PostSerializer
