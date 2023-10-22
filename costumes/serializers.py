from rest_framework import serializers
from costumes.models import Costume
from votes.models import Vote


class CostumeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    vote_id = serializers.SerializerMethodField()
    votes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_vote_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            vote = Vote.objects.filter(
                owner=user, costume=obj
            ).first()
            return vote.id if vote else None
        return None

    class Meta:
        model = Costume
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'vote_id', 'votes_count',
        ]