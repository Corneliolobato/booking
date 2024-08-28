from django.urls import path
from apps.views import *

urlpatterns = [


    path('login/',LoginPage,name='login'),
    path('logout/',LogoutPage,name='logout'),
    path('user/change/password', UserPasswordChange.as_view(), name='user-change-password'),
    path('user/change-user-account', AdminChangeAccount, name='user-change-account'),



    path('admin-panel/', Home, name='admin-panel'),
    path('admin-dashboard/', AdminDashboard, name='admin-dashboard'),

    path('admin-guest/', AdminGuest, name='admin-guest'),
    path('admin-form-guest/', AdminGuestForm, name='admin-guest-form'),
    path('admin-guest/update/<str:id>', AdminGuestUpdate, name='admin-guest-update'),
    path('admin-guest/delete/<str:id>', AdminGuestDelete, name='admin-guest-delete'),

    path('admin-room/', AdminRoom, name='admin-room'),
    path('admin-room-in/', AdminRoomIn, name='admin-room-in'),
    path('admin-form-room/', AdminRoomForm, name='admin-room-form'),
    path('admin-room/update/<str:id>', AdminRoomUpdate, name='admin-room-update'),
    path('admin-room/delete/<str:id>', AdminRoomDelete, name='admin-room-delete'),

    path('admin-staff/', AdminStaff, name='admin-staff'),

    path('admin-reservation/', AdminReservation, name='admin-reservation'),
    path('move_to_reservated/<int:reservation_id>/', move_to_reservated, name='admin-move-reservated'),
    path('reservated_report/', reservated_report, name='reservated-report'),
    path('admin-form-reservation/', AdminReservationForm, name='admin-reservation-form'),
    path('admin-reservation/update/<str:id>', AdminReservationUpdate, name='admin-reservation-update'),
    path('admin-reservation/delete/<str:id>', AdminReservationDelete, name='admin-reservation-delete'),

]
