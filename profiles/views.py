# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import Profile
from .serializers import ProfileSerializer
from fixit_drf_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    Profile creation handled by django signals.
    This returns a list of all profiles.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count("profile_owner__post", distinct=True),
        stars_count=Count('stars', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'stars__owner__profile',
        'status'
    ]
    ordering_fields = [
        'posts_count',
        'stars_count',
        'stars__created_at'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update profiles for authenticated users.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count("profile_owner__post", distinct=True),
        stars_count=Count('stars', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
