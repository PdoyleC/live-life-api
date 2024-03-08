from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    """Serializer for the Trip model."""
    class Meta:
        model = Trip
        fields = [
            'id',
            'name',
            'quantity',
            'buy',
            'created_at',
            'updated_at'
        ]


class TripDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Trip model."""

    class Meta:
        model = Trip
        fields = [
            'id',
            'name',
            'quantity',
            'buy',
            'created_at',
            'updated_at'
        ]
