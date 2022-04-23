from django.contrib import admin

from .models import StaffMember
from django.utils.html import format_html

# Register your models here.
class StaffMembersAdminView(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))
    
    thumbnail.short_description = "photo"
    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date' )# listing in tuples the attributes we 
                                #desire to views ass columns \. Its a tuple with one value
    list_display_links = ('id','thumbnail', 'first_name',) #choosing columns to be clickable
    list_filter = ('designation',)
    search_fields = ('first_name', 'last_name', 'designation') # adding a search bar that filters by the columns listed in the tuple
    
admin.site.register(StaffMember, StaffMembersAdminView)