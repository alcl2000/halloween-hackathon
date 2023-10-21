from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Costume
from .serializers import CostumeSerializer
from app.permissions import IsOwnerOrReadOnly


class CostumeList(APIView):
    """
    List costume posts or create a costume post if logged in
    """
    serializer_class = CostumeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        costumes = Costume.objects.all()
        serializer = CostumeSerializer(
            costumes, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def costume(self, request):
        serializer = CostumeSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class CostumeDetail(APIView):
    """
    Retrieve a costume post and edit or delete it if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CostumeSerializer

    def get_object(self, pk):
        try:
            costume = Costume.objects.get(pk=pk)
            self.check_object_permissions(self.request, costume)
            return costume
        except Costume.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        costume = self.get_object(pk)
        serializer = CostumeSerializer(
            costume, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        costume = self.get_object(pk)
        serializer = CostumeSerializer(
            costume, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        costume = self.get_object(pk)
        costume.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )