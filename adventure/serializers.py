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
            'adv_type',
            'personal_note',
            'created_at'
        ]


class AdventureDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')