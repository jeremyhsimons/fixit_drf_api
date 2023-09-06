from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    post_owner = serializers.ReadOnlyField(source="author.username")
    profile_id = serializers.ReadOnlyField(source="author.profile.id")
    profile_image = serializers.ReadOnlyField(
        source="author.profile.image.url"
    )
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Post
        fields = [
            "id", "author", "created_at",
            "updated_at", "content", "image",
            "category", "is_owner", "profile_id",
            "profile_image", 'post_owner',
        ]
