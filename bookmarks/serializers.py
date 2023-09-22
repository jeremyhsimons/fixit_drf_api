# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from django.db import IntegrityError
from rest_framework import serializers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """
    A serializer to handle bookmark data moving to
    and from the database.
    """
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Bookmark
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
                "detail": "possible bookmark duplication"
            })
