from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from live_life_api.permissions import IsOwnerOrReadOnly
from .models import Trip
from .serializers import TripSerializer, TripDetailSerializer


class TripList(generics.ListCreateAPIView):
    """
    View for creating Trip list.
    """
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Trip.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting Trip list.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TripDetailSerializer
    queryset = Trip.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(owner=user)
