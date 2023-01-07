from os import name
from django.urls import path,include
from django.conf.urls import *
from django.views.generic import TemplateView
from HospitalApp.views import landing , HospitalAuth, dashboard, personalinfo, patient_disease, DoctorAuth
urlpatterns = [
   
    path('',landing.index, name='Home'),
    path('schemes',landing.schemes, name='schemes'),
    path('hospital-login',HospitalAuth.Hospital_login, name='Login'),
    path('hospital-register',HospitalAuth.Hospital_register, name='Register'),
    path('doctor-login',DoctorAuth.Doctor_login, name='DoctorLogin'),
    path('doctor-register',DoctorAuth.Doctor_register, name='DoctorRegister'),
    path('dashboard',dashboard.dash_index, name='Dashboard'),
     path('error',dashboard.error, name='Error'),
    path('personal-info',personalinfo.Add_PersonalInfo, name='AddPatientInfo'),
    path('disease',patient_disease.Add_Disease, name='AddDisease'),
    path('SearchPatient',patient_disease.SearchData, name='SearchData'),
    path('PatientDetails',patient_disease.ViewData, name='ViewData'),
    path('personaldata/<int:pk>/',patient_disease.ViewPersonalData, name='ViewPersonalData'),
    path('diseasedata/<int:pk>/',patient_disease.ViewDiseaseData, name='ViewDiseaseData'),
    path('logout/', HospitalAuth.logoutUser, name='Logout'),
    path('pdf/', personalinfo.GeneratePdf,name="PDF"),
]


