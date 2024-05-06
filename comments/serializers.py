from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    Includes three additional fields when listing Comment instances.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'event',
            'content', 'is_owner', 'profile_id', 'profile_image',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model in detail view.
    The event field is read-only to avoid setting it on updates.
    """
    event = serializers.ReadOnlyField(source='event.id')
