from rest_framework import viewsets
from .models import Guest, Room, Reservation, RoomOccupied, RoomPrice
from .serializers import GuestSerializer, RoomSerializer, ReservationSerializer, RoomOccupiedSerializer, RoomPriceSerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class RoomOccupiedViewSet(viewsets.ModelViewSet):
    queryset = RoomOccupied.objects.all()
    serializer_class = RoomOccupiedSerializer

class RoomPriceViewSet(viewsets.ModelViewSet):
    queryset = RoomPrice.objects.all()
    serializer_class = RoomPriceSerializer
