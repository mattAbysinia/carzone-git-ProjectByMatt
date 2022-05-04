from django.shortcuts import render

from .models import StaffMember
from car_app.models import Car
# Create your views here.
staffMember_global_object= StaffMember()

def home(request):
    staff_members = staffMember_global_object.get_all_staff_members()
    car_object = Car()
    data = {
        'staff_members': staff_members,
        'featured_cars': car_object.get_all_featured_cars(),
        'latest_cars': car_object.get_latest_cars(),
    } 
    return render(request,"pages/home.html", data)
def about(request):
    staff_members = staffMember_global_object.get_all_staff_members()
    data = {
        'teams': staff_members,
    } 
    return render(request,'pages/about.html', data)
def services(request):
    
    return render(request, 'pages/services.html')
def contact(request):
    
    return render(request, 'pages/contact.html')