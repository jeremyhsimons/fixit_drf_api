from rest_framework import generics, permissions
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
