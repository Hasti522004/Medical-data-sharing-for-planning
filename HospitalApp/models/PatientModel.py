from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tbl_patient_information(models.Model):
    # Making one to one relationship with User model of Django
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    AadhaarId = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    address = models.CharField(max_length=253)
    bloodgroup = models.CharField(max_length=50)

    bloodpressure = models.CharField(max_length=500)
    diabetes = models.CharField(max_length=500)
    colestrol = models.CharField(max_length=500)
    familydoctor_name = models.CharField(max_length=50)
    doctor_number = models.CharField(max_length=15)
    allergies = models.CharField(max_length=500)
    surgeryhistory = models.CharField(max_length=500)
    AddedBy= models.IntegerField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name



class tbl_patient_disease(models.Model):
    # Making one to one relationship with User model of Django
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    DiseaseID= models.AutoField(primary_key= True)
    #AadhaarId = models.ForeignKey(tbl_patient_information,on_delete=models.CASCADE)
    AadhaarId = models.IntegerField()
    PatientName = models.CharField(max_length=100)
    PatientNumber = models.CharField(max_length=15)
    DiseaseType = models.CharField(max_length=512)
    ReportDateTime = models.DateTimeField()
    FeesCharged = models.CharField(max_length=512)
    MediclaimRaised  = models.CharField(max_length=15)
    DrugsPrescribed = models.CharField(max_length=512)
    OtherDetails = models.CharField(max_length=512)
    AddedBy= models.IntegerField()
   
    created_at = models.DateTimeField()

    def __str__(self):
        return self.PatientName

