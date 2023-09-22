# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import Comment
from upvotes_comment.models import CommentUpvote


class CommentSerializer(serializers.ModelSerializer):
    """
    A serializer to handle comment data to and from db.
    """
    comment_owner = serializers.ReadOnlyField(source="author.username")
    profile_id = serializers.ReadOnlyField(source="author.profile.id")
    profile_image = serializers.ReadOnlyField(
        source="author.profile.image.url"
    )
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    upvote_id = serializers.SerializerMethodField()
    upvotes_count = serializers.ReadOnlyField()

    def get_upvote_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            upvote = CommentUpvote.objects.filter(
                owner=user, comment=obj
            ).first()
            return upvote.id if upvote else None
        return None

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            "id", "author", "post", "created_at",
            "updated_at", "content",
            "is_owner", "profile_id",
            "profile_image", 'comment_owner', 'upvote_id',
            "upvotes_count",
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Subclass of commentserializer for comment detail view.
    """
    post = serializers.ReadOnlyField(source="post.id")
