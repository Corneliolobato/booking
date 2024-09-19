from django.db import models

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=100)
    sex_choices = [('Male', 'Male'), ('Female', 'Female')]
    sex = models.CharField(max_length=10, choices=sex_choices, default='male')
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        template ='{0.name}'
        return template.format(self)

from django.db import models

class Room(models.Model):
    ROOM_STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
    ]
    
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ROOM_STATUS_CHOICES, default='available')
    images = models.ImageField(upload_to='rooms/', null=True, blank=True)

    def __str__(self):
        return f'Room {self.room_number}'


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservation')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        template = '{0.check_out_date}'
        return template.format(self)
    
class Reservated(models.Model):
    name = models.CharField(max_length=100)
    sex_choices = [('Male', 'Male'), ('Female', 'Female')]
    sex = models.CharField(max_length=10, choices=sex_choices, default='male')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()


    def __str__(self):
        template = '{0.check_out_date}'
        return template.format(self)
    
class RoomOccupied(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='roomoccupiedguest')
    room = models.ForeignKey(Room, on_delete=models.CASCADE,related_name='roomoccupiedroom')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status_choices = [
        ('Ativo', 'Ativo'),
        ('La Ativo', 'La Ativo'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Ativo')

    def __str__(self):
        template = '{0.check_in_date}'
        return template.format(self)
    
class RoomPrice(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Presu", null=True)
    is_active = models.BooleanField(default=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


    def __str__(self):
        template = '{0.price},{0.room_number}'
        return template.format(self)
    

class Amenitiess(models.Model):
    titulu = models.CharField(max_length=50)
    deskrisaun = models.CharField(max_length=225)
    imajen = models.ImageField(upload_to='amenity')
    publication_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    status_choices = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('scheduled', 'Scheduled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='draft')

    
    def __str__(self):
        template = '{0.titulu},{0.deskrisaun}'
        return template.format(self)