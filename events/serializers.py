from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Event
from interested.models import Interested
from attending.models import Attending
from likes.models import Like
from reviews.models import Review


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    attending_id = serializers.SerializerMethodField()
    review_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    interested_count = serializers.ReadOnlyField()
    attending_count = serializers.ReadOnlyField()
    review_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    def validate_event_date(self, value):
        """
        Validates that the event date is not in the past.
        """
        if value < timezone.now().date():
            raise serializers.ValidationError(
                "The date cannot be in the past!")
        return value

    def get_is_owner(self, obj):
        request = self.context.get('request', None)
        if request and hasattr(request, "user"):
            return obj.owner == request.user
        return False

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, event=obj
            ).first()
            return like.id if like else None
        return None

    def get_interested_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            interested = Interested.objects.filter(
                owner=user, event=obj
            ).first()
            return interested.id if interested else None
        return None

    def get_attending_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attending = Attending.objects.filter(
                owner=user, event=obj
            ).first()
            return attending.id if attending else None
        return None

    def get_review_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            review = Review.objects.filter(
                owner=user, event=obj
            ).first()
            return review.id if review else None
        return None

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'description', 'image','is_owner', 'profile_id', 'profile_image', 
            'like_id','attending_id', 'likes_count', 'comments_count', 
            'attending_count','interested_count', 'review_count', 'review_id',
        ]
