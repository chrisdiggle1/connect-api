from django.db import IntegrityError
from rest_framework import serializers
from attending.models import Attending


class AttendingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Attending model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Attending
        fields = ['id', 'created_at', 'owner', 'event']

    def create(self, validated_data):
        """
        Prevents duplicate attendance entries for the same user and event.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You have already confirmed you are going.'
            })
