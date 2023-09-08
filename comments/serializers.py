from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.ReadOnlyField(source="author.username")
    profile_id = serializers.ReadOnlyField(source="author.profile.id")
    profile_image = serializers.ReadOnlyField(
        source="author.profile.image.url"
    )
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Post
        fields = [
            "id", "author", "created_at",
            "updated_at", "content", "image",
            "category", "is_owner", "profile_id",
            "profile_image", 'comment_owner',
        ]


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source="post.id")
