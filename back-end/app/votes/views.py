from rest_framework import generics, permissions
from app.permissions import IsOwnerOrReadOnly
from votes.models import Vote
from votes.serializers import VoteSerializer

	
class VoteList(generics.ListCreateAPIView):
    """
    List votes or create a votes if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a Vote or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
0 comments on commit c3ba26a