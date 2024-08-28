from django import forms 

from apps.models import Guest,Room,Reservation
from django.contrib.auth.models import User

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields =['name','sex', 'email', 'phone']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['images','room_number', 'room_type', 'price','status']

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(forms.ModelForm):
    check_in_date = forms.DateField(label="Check In", widget=DateInput())
    check_out_date = forms.DateField(label="Check Out", widget=DateInput())
    class Meta:
        model = Reservation
        fields = ['guest','room','check_in_date','check_out_date']

class UserChangeAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']