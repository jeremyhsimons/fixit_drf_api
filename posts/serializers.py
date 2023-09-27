# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from rest_framework import serializers
from .models import Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from bookmarks.models import Bookmark
from upvotes_post.models import PostUpvote


class PostSerializer(serializers.ModelSerializer):
    """
    A class to handle post data to and from db
    """
    post_owner = serializers.ReadOnlyField(source="author.username")
    profile_id = serializers.ReadOnlyField(source="author.profile.id")
    profile_image = serializers.ReadOnlyField(
        source="author.profile.image.url"
    )
    is_owner = serializers.SerializerMethodField()
    bookmark_id = serializers.SerializerMethodField()
    upvote_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    upvotes_count = serializers.ReadOnlyField()

    def get_bookmark_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user, post=obj
            ).first()
            return bookmark.id if bookmark else None
        return None

    def get_upvote_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            upvote = PostUpvote.objects.filter(
                owner=user, post=obj
            ).first()
            return upvote.id if upvote else None
        return None

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Post
        fields = [
            "id", "author", "created_at",
            "updated_at", "title", "content", "image",
            "category", "is_owner", "profile_id",
            "profile_image", 'post_owner', 'bookmark_id',
            "upvote_id", "comments_count", "upvotes_count",
        ]
