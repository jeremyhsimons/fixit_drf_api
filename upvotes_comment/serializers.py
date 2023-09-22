# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from django.db import IntegrityError
from rest_framework import serializers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import CommentUpvote


class CommentUpvoteSerializer(serializers.ModelSerializer):
    """
    Handles the data entry for comment upvote instances.
    """
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = CommentUpvote
        fields = [
            "owner",
            "comment",
            "created_at",
            "id"
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                "detail": "possible comment_upvote duplication"
            })
