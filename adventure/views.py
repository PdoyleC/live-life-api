from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from live_life_api.permissions import IsOwnerOrReadOnly
from .models import Adventure
from .serializers import AdventureSerializer, AdventureDetailSerializer


class AdventureList(generics.ListCreateAPIView):
    """
    View for creating adventure post.
    """
    serializer_class = AdventureSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Adventure.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Adventure.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdventureDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting post.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AdventureDetailSerializer
    queryset = Adventure.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Adventure.objects.filter(owner=user)