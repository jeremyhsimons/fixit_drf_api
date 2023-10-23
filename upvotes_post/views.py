"""
Views to handle logic of sending/receiving post upvote data
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from rest_framework import generics, permissions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from fixit_drf_api.permissions import IsBookmarkOwnerOrReadOnly
from .models import PostUpvote
from .serializers import PostUpvoteSerializer


class PostUpvoteList(generics.ListCreateAPIView):
    """
    A view for creating and viewing list of upvote instances.
    """
    serializer_class = PostUpvoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostUpvote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostUpvoteDetail(generics.RetrieveDestroyAPIView):
    """
    A view for retrieving and deleting upvote instances.
    """
    serializer_class = PostUpvoteSerializer
    permission_classes = [IsBookmarkOwnerOrReadOnly]
    queryset = PostUpvote.objects.all()
