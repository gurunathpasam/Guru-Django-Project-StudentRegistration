from django.db import models
from django.db import connection

# Create your models here.
class Students(models.Model):
    firstName=models.CharField(max_length=122)
    middleName=models.CharField(max_length=122)
    lastName=models.CharField(max_length=122)
    dob=models.CharField(max_length=20)
    email=models.CharField(max_length=122)
    contactNumber=models.CharField(max_length=12)
    course=models.CharField(max_length=20)
    academicPercentage=models.CharField(max_length=5)
    activeBacklogs=models.CharField(max_length=10)
    streetAddress=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    state=models.CharField(max_length=122)
    country=models.CharField(max_length=122)









