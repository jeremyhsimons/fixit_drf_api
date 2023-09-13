from rest_framework import generics, permissions
from fixit_drf_api.permissions import IsBookmarkOwnerOrReadOnly
from .models import Star
from .serializers import StarSerializer


class StarList(generics.ListCreateAPIView):
    """
    Handles the creation and retrieving a list of
    star instances.
    """
    serializer_class = StarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Star.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
