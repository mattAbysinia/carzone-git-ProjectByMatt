from django.shortcuts import render

from .models import StaffMember
# Create your views here.

def home(request):
    staff_members = StaffMember.get_all_staff_members()
    data = {
        'staff_members': staff_members,
    } 
    return render(request,"pages/home.html", data)
def about(request):
    staff_members = StaffMember.get_all_staff_members()
    data = {
        'teams': staff_members,
    } 
    return render(request,'pages/about.html', data)
def services(request):
    
    return render(request, 'pages/services.html')
def contact(request):
    
    return render(request, 'pages/contact.html')