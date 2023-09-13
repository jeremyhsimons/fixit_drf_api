from django.db import IntegrityError
from rest_framework import serializers
from .models import Star


class StarSerializer(serializers.ModelSerializer):
    """
    A serializer to handle star data entering the db.
    """
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Star
        fields = [
            "owner",
            "profile",
            "created_at",
            "id"
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                "detail": "possible star duplication"
            })
