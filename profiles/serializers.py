from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    profile_owner = serializers.ReadOnlyField(source="profile_owner.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.profile_owner

    class Meta:
        model = Profile
        fields = [
            "id", "profile_owner", "created_at",
            "updated_at", "name", "bio", "image",
            "status", "is_owner",
        ]
