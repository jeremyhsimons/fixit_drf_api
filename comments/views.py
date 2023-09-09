from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from fixit_drf_api.permissions import IsPostCommentOwnerOrReadOnly


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsPostCommentOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
