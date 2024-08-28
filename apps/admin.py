from django.contrib import admin

# Register your models here.
from apps.models import *

admin.site.register([Guest,Room,Reservation,Reservated,RoomOccupied,RoomPrice])