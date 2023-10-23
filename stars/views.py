"""
Views to handle logic of sending/receiving bookmark data
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3rd party imports
from rest_framework import generics, permissions
from fixit_drf_api.permissions import IsBookmarkOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal imports
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


class StarDetail(generics.RetrieveDestroyAPIView):
    """
    Handles the retrieval and deletion of star instances.
    """
    serializer_class = StarSerializer
    permission_classes = [IsBookmarkOwnerOrReadOnly]
    queryset = Star.objects.all()
