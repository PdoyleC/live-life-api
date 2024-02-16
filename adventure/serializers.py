from rest_framework import serializers
from .models import Adventure


class AdventureSerializer(serializers.ModelSerializer):
    """
    Serializer for the Adventures model
    Adds handles for uers post
    """

    class Meta:
        model = Adventure
        fields = [
            'id',
            'location',
            'activity',
            'personal_note',
            'created_at',
            'image'
        ]


class AdventureDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the detailed Adventures model
    """
    
    class Meta:
        model = Adventure
        fields = [
            'id',
            'location',
            'activity',
            'personal_note',
            'created_at',
            'image'
        ]