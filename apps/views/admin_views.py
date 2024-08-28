from django.shortcuts import render,redirect
from apps.models import Guest, Room, Reservation, Reservated, RoomOccupied
from django.utils import timezone
from rest_framework import viewsets

from apps.forms import GuestForm,RoomForm,ReservationForm,UserChangeAccountForm
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
                return redirect('admin-panel')
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

def AdminGuest(request):
    dados_guest = Guest.objects.all()
    context = {
        'title': 'admin-guest',
        'guest': dados_guest,
        'title': "Admin Guest "
    
    }
    return render(request, 'admin/guest/guest.html',context)

def AdminGuestForm(request):
    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('admin-guest')
    else:
        form = GuestForm()
        
        context = {
            'form': form,
            'title': "Admin Form"
        }
        return render(request, 'admin/guest/guest_form.html', context)
    
def AdminGuestUpdate(request, id):
    data_Guest = Guest.objects.get(id=id)
    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES, instance=data_Guest)
        form.save()
        return redirect('admin-guest')
    else:
        form = GuestForm(instance=data_Guest)

    context = {
        'title': "Formula Atualizar",
        'form': form
    }
    return render(request, 'admin/guest/guest_form.html', context)

def AdminGuestDelete(request, id):
    data_Guest = Guest.objects.get(id=id)
    data_Guest.delete()
    return redirect('admin-guest')


def AdminRoom(request):
    dados_room = Room.objects.all()
    context = {
        'title': 'admin-room',
        'room': dados_room,
        'title': "Admin Room "
    
    }
    return render(request, 'admin/room/room.html',context)

def AdminRoomIn(request):
    dados_room = Room.objects.all()
    context = {
        'title': 'admin-room in',
        'room': dados_room,
        'title': "Admin Room In "
    
    }
    return render(request, 'admin/room/room_in.html',context)


def AdminRoomForm(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('admin-room')
    else:
        form = RoomForm()
        
        context = {
            'form': form,
            'title': "Admin Room Form"
        }
        return render(request, 'admin/room/room_form.html', context)
    
def AdminRoomUpdate(request, id):
    data_Room = Room.objects.get(id=id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=data_Room)
        form.save()
        return redirect('admin-room')
    else:
        form = RoomForm(instance=data_Room)

    context = {
        'title': "Formula Atualizar",
        'form': form
    }
    return render(request, 'admin/room/room_form.html', context)

def AdminRoomDelete(request, id):
    data_Room = Room.objects.get(id=id)
    data_Room.delete()
    return redirect('admin-room')



def AdminReservation(request):
    dados_reser = Reservation.objects.all()
    
    context = {
        'title': 'admin-reservation',
        'reservation': dados_reser
    
    }
    return render(request, 'admin/reservation/reservation.html',context)


from django.shortcuts import get_object_or_404, redirect


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

def reservated_report(request):
    # Fetch all reservated entries
    reservated_entries = Reservated.objects.all()
    
    # Pass the data to the template
    context = {
        'reservated_move': reservated_entries,
    }
    
    return render(request, 'admin/reservation/report.html', context)



def AdminReservationForm(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('admin-reservation')
    else:
        form = ReservationForm()
        
        context = {
            'form': form,
            'title': "Admin Reservation Form"
        }
        return render(request, 'admin/reservation/reservation_form.html', context)
    
def AdminReservationUpdate(request, id):
    data_Reservation = Reservation.objects.get(id=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES, instance=data_Reservation)
        form.save()
        return redirect('admin-reservation')
    else:
        form = ReservationForm(instance=data_Reservation)

    context = {
        'title': "Formula Atualizar",
        'form': form
    }
    return render(request, 'admin/reservation/reservation_form.html', context)

def AdminReservationDelete(request, id):
    data_Reservation = Reservation.objects.get(id=id)
    data_Reservation.delete()
    return redirect('admin-reservation')

def AdminStaff(request):
    data_roccupied = RoomOccupied.objects.all()
    context = {
        'data_roccupied': data_roccupied
    }
    return render(request, 'admin/resepsionist/resepsionist.html',context)
