from rest_framework import serializers
from .models import Interested
from django.db import IntegrityError


class InterestedSerializer(serializers.ModelSerializer):
    """
    Serializer for the Interested model.
    Represents a user's interest in an event.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    event_name = serializers.ReadOnlyField(source='event.title')

    class Meta:
        model = Interested
        fields = ['id', 'owner', 'event', 'event_name', 'created_at']

    def create(self, validated_data):
        """
        Ensure unique interest entry.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You have already shown interest in this event!'
            })
