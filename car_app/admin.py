from django.contrib import admin
from django.utils.html import format_html
from .models import Car
# Register your models here.

class CarsAdminView(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))
    
    thumbnail.short_description = "Car_Photo"
    list_display = ('id','car_title', 'thumbnail', 'body_style', 'state', 'year','is_featured' )# listing in tuples the attributes we 
                                #desire to views ass columns \. Its a tuple with one value
    list_display_links = ('id','car_title', 'thumbnail' ) #choosing columns to be clickable
    list_filter = ('city', 'fuel_type', 'body_style' ,'model','transmission_type','year')
    search_fields = ('car_title', 'city', 'body_style','model', 'state','transmission_type','year' ) # adding a search bar that filters by the columns listed in the tuple
    list_editable = ('is_featured','year')
admin.site.register(Car, CarsAdminView)