from rest_framework import serializers
from .models import Post
from bookmarks.models import Bookmark
from upvotes_post.models import PostUpvote


class PostSerializer(serializers.ModelSerializer):
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

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Post
        fields = [
            "id", "author", "created_at",
            "updated_at", "content", "image",
            "category", "is_owner", "profile_id",
            "profile_image", 'post_owner', 'bookmark_id',
            "upvote_id", "comments_count", "upvotes_count",
        ]
