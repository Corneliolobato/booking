from django.shortcuts import render,redirect,get_object_or_404
from apps.models import Guest, Room, Reservation, Reservated, RoomOccupied, Amenitiess
from django.utils import timezone
from rest_framework import viewsets

from apps.forms import GuestForm,RoomForm,ReservationForm,UserChangeAccountForm,AmenitiesForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
@login_required
def Home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'admin/home.html',context)


def LoginPage(request):
    if  request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
                login(request,user)
                return redirect('admin-dashboard')
        else:
                messages.error(request,'Username and Password failed please once')

    context = {
        "title": 'pajina login',
    }
    return render(request,'auth/login.html',context)

@login_required
def LogoutPage(request):
	logout(request)
	return render(request,'auth/logout.html')


from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
class  UserPasswordChange(PasswordChangeView):
    template_name = 'auth/change_password.html'
    success_url = reverse_lazy('user-change-password')
    def get_success_url(self):
        messages.success(self.request, 'Password Was Successfully Changed.')
        return super().get_success_url()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
class  UserPasswordChange(PasswordChangeView):
    template_name = 'auth/change_password.html'
    success_url = reverse_lazy('user-change-password')
    def get_success_url(self):
        messages.success(self.request, 'Password Was Successfully Changed.')
        return super().get_success_url()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def AdminChangeAccount(request):
    loginUser = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = UserChangeAccountForm(request.POST,instance=loginUser)
        if form.is_valid():
            form.save()
            messages.success(request,f'Ita boot nia konta Uzuario Atualizado')
            return redirect('user-change-account')
    else:
        form = UserChangeAccountForm(instance=loginUser)

    context = {
        'form' : form,
        'title': "Change Account"
        
    }
    return render(request, 'admin/admin_profile.html',context)





class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    


@login_required
def AdminDashboard(request):
    today = timezone.now().date()
    total_guest = Guest.objects.count()
    total_room = Room.objects.count()
    context = {
        'title': 'Dashboard',
        'tguest': total_guest,
        'troom': total_room,
        'today': today
        
    }
    return render(request, 'admin/dashboard.html',context)

@login_required
def AdminGuest(request):
    dados_guest = Guest.objects.all()
    context = {
        'title': 'admin-guest',
        'guest': dados_guest,
        'title': "Admin Guest "
    
    }
    return render(request, 'admin/guest/guest.html',context)

@login_required
def AdminGuestForm(request):
    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Dadus Bainaka Rai ho Successfully')
        return redirect('admin-guest')
    else:
        form = GuestForm()
        
        context = {
            'form': form,
            'title': "Admin Form"
        }
        return render(request, 'admin/guest/guest_form.html', context)
    
@login_required   
def AdminGuestUpdate(request, id):
    data_Guest = Guest.objects.get(id=id)
    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES, instance=data_Guest)
        form.save()
        messages.success(request,'Dadus Bainaka Atualizadu Successfully')
        return redirect('admin-guest')
    else:
        form = GuestForm(instance=data_Guest)

    context = {
        'title': "Formula Atualizar",
        'form': form    
    }
    return render(request, 'admin/guest/guest_form.html', context)


@login_required
def AdminGuestDelete(request, id):
    data_Guest = Guest.objects.get(id=id)
    data_Guest.delete()
    return redirect('admin-guest')

@login_required
def AdminRoom(request):
    dados_room = Room.objects.all()
    context = {
        'title': 'admin-room',
        'room': dados_room,
        'title': "Admin Room "
    
    }
    return render(request, 'admin/room/room.html',context)

@login_required
def AdminRoomIn(request):
    dados_room = Room.objects.all()
    context = {
        'title': 'admin-room in',
        'room': dados_room,
        'title': "Admin Room In "
    
    }
    return render(request, 'admin/room/room_in.html',context)

@login_required
def AdminRoomForm(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kamar berhasil disimpan.')
            return redirect('admin-room')
        else:
            messages.error(request, 'Ada kesalahan dalam form. Mohon periksa kembali.')
    else:
        form = RoomForm()
        
    context = {
        'form': form,
        'title': "Admin Room Form"
    }
    return render(request, 'admin/room/room_form.html', context)
    
@login_required  
def AdminRoomUpdate(request, id):
    data_Room = Room.objects.get(id=id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=data_Room)
        form.save()
        messages.success(request,'Dadus Kuartu Atualizadu Successfully')
        return redirect('admin-room')
    else:
        form = RoomForm(instance=data_Room)

    context = {
        'title': "Formula Atualizar",
        'form': form
    }
    return render(request, 'admin/room/room_form.html', context)

@login_required
def AdminRoomDelete(request, id):
    data_Room = Room.objects.get(id=id)
    data_Room.delete()
    return redirect('admin-room')




@login_required
def AdminAmenities(request):
    dados_amenity = Amenitiess.objects.all()
    context = {
        'title': 'admin-amenities',
        'amenity': dados_amenity,
        'title': "Admin Amenities "
    
    }
    return render(request, 'admin/amenities/amenity.html',context)

@login_required
def AdminAmenityForm(request):
    if request.method == 'POST':
        form = AmenitiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dadus Rai ho Susesu!.')
            return redirect('admin-amenity')
        else:
            messages.error(request, 'Ada kesalahan dalam form. Mohon periksa kembali.')
    else:
        form = AmenitiesForm()
        
    context = {
        'form': form,
        'title': "Admin Amenities Form"
    }
    return render(request, 'admin/amenities/amenity_form.html', context)
    
@login_required  
def AdminAmenityUpdate(request, id):
    data_amenity = Amenitiess.objects.get(id=id)
    if request.method == 'POST':
        form = AmenitiesForm(request.POST, request.FILES, instance=data_amenity)
        form.save()
        messages.success(request,'Dadus Amenity Atualizadu ho Susesu!')
        return redirect('admin-amenity')
    else:
        form = AmenitiesForm(instance=data_amenity)

    context = {
        'title': "Formula Atualizar",
        'form': form
    }
    return render(request, 'admin/amenities/amenity_form.html', context)

@login_required
def AdminAmenityDelete(request, id):
    data_amenity = Amenitiess.objects.get(id=id)
    data_amenity.delete()
    return redirect('admin-amenity')




@login_required
def AdminLoadUpdateForm(request):
	if request.method == 'GET':
		object_id = request.GET.get('objectID')
		objects = get_object_or_404(Amenitiess,id=object_id)
		form = AmenitiesForm(instance=objects)
	context = {
		'form':form,
		'objects':objects,
	}
	return render(request,'admi/admin_load_form.html',context)









@login_required
def AdminReservation(request):
    dados_reser = Reservation.objects.all()
    
    context = {
        'title': 'admin-reservation',
        'reservation': dados_reser
    
    }
    return render(request, 'admin/reservation/reservation.html',context)


from django.shortcuts import get_object_or_404, redirect

@login_required
def move_to_reservated(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservations = Reservation.objects.all()  # Fetch all reservations

    
    
    # Create a new entry in the Reservated table
    Reservated.objects.create(
        name=reservation.guest.name,  # Access the name from the Guest model
        sex=reservation.guest.sex,    # Access the sex from the Guest model
        email=reservation.guest.email, # Access the email from the Guest model
        phone=reservation.guest.phone, # Access the phone from the Guest model
        room=reservation.room,
        check_in_date=reservation.check_in_date,
        check_out_date=reservation.check_out_date,
    )
    
    # Delete the data from the Reservation table
    reservation.delete()

    reservated = Reservated.objects.all()    
    # Redirect or provide a response after completion
    context ={
        'reservated' : reservated,
    }
    
    return render(request, 'admin/reservation/reservated_report.html',context)




# Ubah ke halaman yang sesuai
@login_required
def reservated_report(request):
    # Fetch all reservated entries
    reservated_entries = Reservated.objects.all()
    
    # Pass the data to the template
    context = {
        'reservated_move': reservated_entries,
    }
    
    return render(request, 'admin/reservation/report.html', context)

@login_required
def reservated_report_delete(request, id):
    data_Reservation = Reservated.objects.get(id=id)
    data_Reservation.delete()
    return redirect('reservated-report')


@login_required

def AdminReservationForm(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the reservation
            reservation = form.save(commit=False)
            room = reservation.room
            
            # Check if the room is still available before saving
            if room.status == 'occupied':
                messages.error(request, 'Kamar yang dipilih sudah dipesan.')
                return render(request, 'admin/reservation/reservation_form.html', {'form': form, 'title': "Admin Reservation Form"})
            
            reservation.save()
            
            # Update room status to occupied
            room.status = 'occupied'
            room.save()
            
            messages.success(request, f'The Room {room.room_number} Reservated.')
            return redirect('admin-reservation')
        else:
            messages.error(request, 'Ada kesalahan dalam form reservasi. Mohon periksa kembali.')
    else:
        form = ReservationForm()
        
    context = {
        'form': form,
        'title': "Admin Reservation Form"
    }
    return render(request, 'admin/reservation/reservation_form.html', context)
@login_required   
def AdminReservationUpdate(request, id):
    data_Reservation = Reservation.objects.get(id=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES, instance=data_Reservation)
        form.save()
        messages.success(request,'Dadus Reservatsaun Atualizadu Successfully')
        return redirect('admin-reservation')
    else:
        form = ReservationForm(instance=data_Reservation)

    context = {
        'title': "Formula Atualizar",
        'form': form
    }
    return render(request, 'admin/reservation/reservation_form.html', context)

@login_required
def AdminReservationDelete(request, id):
    data_Reservation = Reservation.objects.get(id=id)
    data_Reservation.delete()
    return redirect('admin-reservation')

@login_required
def AdminStaff(request):
    data_roccupied = RoomOccupied.objects.all()
    context = {
        'data_roccupied': data_roccupied
    }
    return render(request, 'admin/resepsionist/resepsionist.html',context)





from django.http import JsonResponse
import json

@login_required
def perform_amenity_action(request):
    if request.method == 'POST':
        # Mendapatkan data dari POST
        checked_items = request.POST.get('checkedItems', '').strip()  # Menghilangkan spasi ekstra
        action_type = request.POST.get('actionType')

        # Cek apakah tidak ada data yang dipilih
        if not checked_items:
            messages.error(request, 'Oops! Ita boot seidauk hili dadus ruma.')
            return redirect('admin-amenity')

        # Split IDs hanya jika ada checked items
        ids = checked_items.split(',')

        # Proses tindakan berdasarkan tipe
        if action_type == 'delete':
            for i in ids:
                data = get_object_or_404(Amenitiess, id=i)
                data.delete()
            messages.success(request, 'Dados Publikasaun nebe ita boot hili, Delete ona ho susesu!')
            return redirect('admin-amenity')

        elif action_type == 'publishCheckedPost':
            for i in ids:
                data = get_object_or_404(Amenitiess, id=i)
                data.status = 'Published'
                data.save()
            messages.success(request, 'Dados Publikasaun nebe ita boot hili, publika ona ho susesu!')
            return redirect('admin-amenity')

        elif action_type == 'draftCheckedPost':
            for i in ids:
                data = get_object_or_404(Amenitiess, id=i)
                data.status = 'Draft'
                data.save()
            messages.success(request, 'Dados Publikasaun nebe ita boot hili, draft ona ho susesu!')
            return redirect('admin-amenity')

        else:
            return JsonResponse({'error': 'Invalid action type.'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    
from django.http import JsonResponse
