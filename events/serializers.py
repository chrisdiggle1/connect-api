from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request', None)
        if request and hasattr(request, "user"):
            return obj.owner == request.user
        return False

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'description',
            'image', 'event_date', 'category', 'is_owner'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']