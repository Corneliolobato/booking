from rest_framework import serializers
from .models import Guest, Room, Reservation, RoomOccupied, RoomPrice

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class RoomOccupiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomOccupied
        fields = '__all__'

class RoomPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPrice
        fields = '__all__'
