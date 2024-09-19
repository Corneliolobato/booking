from django.shortcuts import render,redirect,get_object_or_404
from apps.models import Amenitiess,Room
from apps.forms import ReservatedForm,Reservation,Guest
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
        'title' : "portfolio",
        'portfolio_active': "active",
        'room' : dados_room
        
    }
    return render(request, 'rooms.html',context)


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    
    if request.method == 'POST':
        form = ReservatedForm(request.POST)
        if form.is_valid():
            # Save Reservated form and create a Reservation instance
            reservated_instance = form.save(commit=False)
            reservated_instance.room = room  # Assign the selected room
            reservated_instance.save()

            # Create a Reservation entry in the system
            guest, created = Guest.objects.get_or_create(
                name=reservated_instance.name,
                email=reservated_instance.email,
                phone=reservated_instance.phone
            )

            Reservation.objects.create(
                guest=guest,
                room=room,
                check_in_date=reservated_instance.check_in_date,
                check_out_date=reservated_instance.check_out_date
            )

            # Redirect to success page
            return redirect('booking_success')
    else:
        form = ReservatedForm()

    context = {
        'form': form,
        'room': room
        
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

