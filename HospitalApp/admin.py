
from django.contrib import admin
from HospitalApp.models.HospitalAuthModel import tbl_hospital_register
from HospitalApp.models.PatientModel import tbl_patient_information, tbl_patient_disease

# Register your models here.

admin.site.register(tbl_hospital_register)

admin.site.register(tbl_patient_information)
admin.site.register(tbl_patient_disease)



