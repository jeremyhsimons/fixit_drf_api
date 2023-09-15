from rest_framework import generics, permissions
from fixit_drf_api.permissions import IsBookmarkOwnerOrReadOnly
from .models import CommentUpvote
from .serializers import CommentUpvoteSerializer


class CommentUpvoteList(generics.ListCreateAPIView):
    """
    A view for creating and viewing a list of
    comment upvote instances.
    """
    serializer_class = CommentUpvoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CommentUpvote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentUpvoteDetail(generics.RetrieveDestroyAPIView):
    """
    A view for retrieving and deleting
    comment upvote instances.
    """
    serializer_class = CommentUpvoteSerializer
    permission_classes = [IsBookmarkOwnerOrReadOnly]
    queryset = CommentUpvote.objects.all()
