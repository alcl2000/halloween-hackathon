from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from costumes.models import Costume
from favorites.models import Favorite
from favorites.serializers import FavoriteSerializer


class FavoriteCostumePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, costume_id):
        try:
            costume = Costume.objects.get(pk=costume_id)
        except Costume.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Check if the user has already saved the costume post
        favorite_post, created = Favorite.objects.get_or_create(owner=request.user, post=costume)

        if created:
            serializer = FavoriteSerializer(favorite_post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        favorite_post.delete()
        return Response({'detail': 'Post unsaved successfully.'}, status=status.HTTP_200_OK)

	
class FavoriteList(generics.ListCreateAPIView):
    """
    List Favorite costume posts for the authenticated user.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(owner=user)


class FavoriteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a Favorite or delete it by id if you own it.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()