from django.db import IntegrityError
from rest_framework import serializers
from favorites.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Favorite model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorite
        fields = ['id', 'created_at', 'owner', 'post']
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })