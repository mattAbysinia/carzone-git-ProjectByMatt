from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.

class Car(models.Model):
    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))
        #class variables
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
        
    body_style = models.CharField(max_length=100)
    car_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True, null=True)
    car_photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True, null=True)
    car_photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True, null=True)
    car_photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True, null=True)
    car_title = models.CharField(max_length=255)
    city = models.CharField(max_length=100)#charField should be used for holding 255 character
    color = models.CharField(max_length=100)#charField should be used for holding 255 character
    condition = models.CharField(max_length=100)#charField should be used for holding 255 character
    created_date = models.DateTimeField(auto_now_add=True)
    description = RichTextField()#ckeditor richtextfield 
    engine = models.CharField(max_length=100)
    features = MultiSelectField(choices=features_choices)
    fuel_type = models.CharField(max_length=50)
    interior = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    milage = models.IntegerField()
    miles = models.IntegerField()
    model = models.CharField(max_length=100)
    number_of_doors = models.CharField(choices=door_choices, max_length=10)
    number_of_previous_owners = models.IntegerField()
    passangers = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(choices =state_choice, max_length=100)
    transmission_type = models.CharField(max_length=100)
    vin_number = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    
    def __str__(self) -> str:
        return f"id= {self.id} | {self.car_title}"
    
    def get_all_featured_cars(self) -> object:
        try:
            featured_cars = Car.objects.filter(is_featured=True).order_by('-id')
            return featured_cars
        except:
            print("__________________________Error getting All featured cars __________________")          
            print("__________________________Error getting All featured cars Ends Here __________________")
            
        return None
    
    def get_latest_cars(self) -> object:
        try:
            latest_cars = Car.objects.all().order_by('-id')
            return latest_cars
        except:
            print('_______________________Error getting latest cars_______________')
        return None