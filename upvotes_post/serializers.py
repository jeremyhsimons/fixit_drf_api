from django.db import IntegrityError
from rest_framework import serializers
from .models import PostUpvote


class PostUpvoteSerializer(serializers.ModelSerializer):
    """
    Handles the data entry for post upvote instances.
    """
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = PostUpvote
        fields = [
            "owner",
            "post",
            "created_at",
            "id"
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                "detail": "possible post_upvote duplication"
            })
