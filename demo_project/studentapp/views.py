from django.shortcuts import render
from django.http import HttpResponse
from studentapp.models import Students

# Create your views here.

def home(request):
    if request.method=="POST":
        firstName=request.POST.get('firstName')
        middleName=request.POST.get('middleName')
        lastName=request.POST.get('lastName')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        contactNumber=request.POST.get('contactNumber')
        course=request.POST.get('course')
        academicPercentage=request.POST.get('academicPercentage')
        activeBacklogs=request.POST.get('activeBacklogs')
        streetAddress=request.POST.get('streetAddress')
        academicPercentage=request.POST.get('academicPercentage')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')
        home2=Students(firstName=firstName,middleName=middleName,lastName=lastName,dob=dob,email=email,contactNumber=contactNumber,course=course,
                       academicPercentage=academicPercentage,activeBacklogs=activeBacklogs,streetAddress=streetAddress,city=city,
                       state=state,country=country)
        home2.save()
    return render(request,"home.html")