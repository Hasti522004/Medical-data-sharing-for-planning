from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tbl_hospital_register(models.Model):
    # Making one to one relationship with User model of Django
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    address = models.CharField(max_length=253)
    doctor_name = models.CharField(max_length=100)
  

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class tbl_doctor_register(models.Model):
    # Making one to one relationship with User model of Django
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    DoctorID= models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=512)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    education = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
