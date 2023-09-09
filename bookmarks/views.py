from rest_framework import generics, permissions
from fixit_drf_api.permissions import IsBookmarkOwnerOrReadOnly
from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkListView(generics.ListCreateAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [IsBookmarkOwnerOrReadOnly]
    queryset = Bookmark.objects.all()
