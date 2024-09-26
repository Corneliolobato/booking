from django.shortcuts import render,redirect,get_object_or_404
from apps.models import Amenitiess,Room,Reservation,Guest,Reservated
from apps.forms import ReservatedForm
from django.contrib import messages
# from main.models import *



def AmenitiesPost(request):
    dados_amen = Amenitiess.objects.filter(status="Published").all()
    post_image_urls = []
    for post in dados_amen:
        image_urls, text = extract_images_from_post_content(post.deskrisaun)  # Adjust field name as necessary
        _, words50 = extract_total_words(text)
        post_image_urls.append({
            'id': post.id,
            'title': post.titulu,
            'image': image_urls,
            'deskrisaun': words50,
            'publication_date': post.publication_date
        })

    print('post_image_urls :', post_image_urls)

    context = {
        'title': "Hotel Amenities",
        'post_active': "active",
        'post': dados_amen,
        'post_image_url': post_image_urls
    }
    return render(request, 'index.html', context)




def PublicRoom(request):
    dados_room = Room.objects.all()
    print(dados_room)
    context = {
        'title' : "Rooms ",
        'portfolio_active': "active",
        'room' : dados_room
        
    }
    return render(request, 'rooms.html',context)

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    
    if request.method == 'POST':
        form = ReservatedForm(request.POST)
        
        # Create a Reservated instance but do not save yet
        reservated_instance = form.save(commit=False)
        
        # Assign the selected room to the reservated_instance
        reservated_instance.room = room  # Assign the selected room
        
        if form.is_valid():  # Check if the form is valid
            reservated_instance.save()  # Save the Reservated instance
            
            # Create or get the guest instance
            guest, created = Guest.objects.get_or_create(
                name=reservated_instance.name,
                email=reservated_instance.email,
                phone=reservated_instance.phone,
                defaults={'sex': reservated_instance.sex.capitalize()}
            )

            # Add a success message
            messages.success(request, f'New reservation created by {reservated_instance.name}')

            # Create a Reservation entry
            Reservation.objects.create(
                guest=guest,
                room=room,
                check_in_date=reservated_instance.check_in_date,
                check_out_date=reservated_instance.check_out_date
            )

            # Mark the room as occupied
            room.status = 'occupied'  # Assuming 'occupied' is the status for booked rooms
            room.save()

            # Redirect to success page
            return redirect('booking_success')
    else:
        form = ReservatedForm()  # Create an empty form for GET request

    context = {
        'form': form,
        'room': room,
        'title': "Details"
    }
    return render(request, 'detail_room.html', context)


def booking_success(request):
    return render(request, 'booking_success.html')



from bs4 import BeautifulSoup

def extract_images_from_post_content(deskrisaun):
    soup = BeautifulSoup(deskrisaun, 'html.parser')

    #Find all images tags in the content
    images = soup.find_all('img')

    text = soup.get_text(separator=' ')
    text = ' '.join(text.split())

    #Extract the src atributes of each image tag
    image_url = [img['src'] for img in images]

    #Return the list of images URLS
    return image_url,text

def extract_total_words(text):
    #split the text into words
    words = text.split()

    #Take the first 100 words and split them
    words20 = ' '.join(words[:20])
    words50 = ' '.join(words[:50])

    return words20,words50

