from django.db import models

# Create your models here.

class StaffMember(models.Model):
   first_name = models.CharField(max_length= 255)
   last_name = models.CharField(max_length= 255)
   designation = models.CharField(max_length= 255)
   photo = models.ImageField(upload_to='photos/%Y/%m/%d/') # y current year, m current month, d current day
   #create a directory photos/current_year/current_month/current_day
   facebook_link = models.URLField(max_length = 100) 
   twitter_link = models.URLField(max_length = 100) 
   google_plus_link = models.URLField(max_length = 100) 
   created_date = models.DateTimeField(auto_now_add = True)
   
   def get_all_staff_members(self):
       try:
           all_staff_members = StaffMember.objects.all()
           return all_staff_members
       except:
           print("++++ error readind all staff members")
        
   def __str__(self):
       
       return f'{self.first_name }  {self.last_name} | {self.designation} '
