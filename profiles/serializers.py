# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from rest_framework import serializers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import Profile
from stars.models import Star


class ProfileSerializer(serializers.ModelSerializer):
    """
    A serializer to handle profile data to and from the db.
    """
    profile_owner = serializers.ReadOnlyField(source="profile_owner.username")
    is_owner = serializers.SerializerMethodField()
    star_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    stars_count = serializers.ReadOnlyField()

    def get_star_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            star = Star.objects.filter(
                owner=user, profile=obj
            ).first()
            return star.id if star else None
        return None

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.profile_owner

    class Meta:
        model = Profile
        fields = [
            "id", "profile_owner", "created_at",
            "updated_at", "name", "bio", "image",
            "status", "is_owner", 'star_id',
            "posts_count", "stars_count"
        ]
