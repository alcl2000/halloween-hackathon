from rest_framework import generics, permissions
from app.permissions import IsOwnerOrReadOnly
from .models import Costume
from .serializers import CostumeSerializer


class CostumeList(generics.ListCreateAPIView):
    """
    List costumes or create a post if logged in
    The perform_create method associates the costume post with the logged in user.
    """
    serializer_class = CostumeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Costume.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CostumeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a costume post and edit or delete it if you own it.
    """
    serializer_class = CostumeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Costume.objects.all()