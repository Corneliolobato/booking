from django import forms 
from django_summernote.widgets import SummernoteWidget

from apps.models import Guest,Room,Reservation,Amenitiess,Reservated
from django.contrib.auth.models import User

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields =['name','sex', 'email', 'phone']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['images', 'room_number', 'room_type', 'price', 'status']

    # Optional: Customizing widgets
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.Select(choices=Room.ROOM_STATUS_CHOICES)
        
    # Optional: Custom validation
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price


class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(forms.ModelForm):
    check_in_date = forms.DateField(
        label="Check In",
        widget=DateInput(attrs={'type': 'date'})  # Use HTML5 date input
    )
    check_out_date = forms.DateField(
        label="Check Out",
        widget=DateInput(attrs={'type': 'date'})  # Use HTML5 date input
    )

    class Meta:
        model = Reservation
        fields = ['guest', 'room', 'check_in_date', 'check_out_date']

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        # Filter rooms that are available
        self.fields['room'].queryset = Room.objects.filter(status='available')

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')
        room = cleaned_data.get('room')

        # Ensure check-in date is before check-out date
        if check_in_date and check_out_date and check_in_date >= check_out_date:
            self.add_error('check_out_date', 'Tanggal check-out harus setelah tanggal check-in.')

        # Ensure room is available
        if room:
            # Check for overlapping reservations
            overlapping_reservations = Reservation.objects.filter(
                room=room,
                check_in_date__lt=check_out_date,
                check_out_date__gt=check_in_date
            )
            if overlapping_reservations.exists():
                self.add_error('room', 'Kamar yang dipilih sudah dipesan pada tanggal tersebut.')

        return cleaned_data
    
class UserChangeAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class AmenitiesForm(forms.ModelForm):
    deskrisaun = forms.CharField(
        label="Deskrisaun",
        required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '500px'}}))
    class Meta:
        model = Amenitiess
        fields = ['titulu','deskrisaun','imajen']


class ReservatedForm(forms.ModelForm):
    class Meta:
        model = Reservated
        fields = ['name', 'sex', 'email', 'phone', 'room', 'check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        # Ambil tanggal check-in dan check-out dari kwargs jika ada
        check_in_date = kwargs.pop('check_in_date', None)
        check_out_date = kwargs.pop('check_out_date', None)
        
        super().__init__(*args, **kwargs)

        # Filter kamar yang sudah dipesan
        if check_in_date and check_out_date:
            self.fields['room'].queryset = Room.objects.filter(
                status='available'
            ).exclude(
                id__in=Reservated.objects.filter(
                    check_in_date__lt=check_out_date,
                    check_out_date__gt=check_in_date
                ).values_list('room_id', flat=True)
            )
        else:
            self.fields['room'].queryset = Room.objects.filter(status='available')