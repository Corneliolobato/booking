from django.urls import path
from apps.views import *

urlpatterns = [

    path('',AmenitiesPost, name='post'),
    path('rooms/',PublicRoom, name='room'),
    path('post-detail/<str:room_id>',room_detail,name='detailroom'),
    path('booking-success/',booking_success, name='booking_success'),
    
]
