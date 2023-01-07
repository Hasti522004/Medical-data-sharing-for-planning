from django.shortcuts import redirect, render
from datetime import date
from xmlrpc.client import DateTime
from django.contrib import messages
from HospitalApp.models.PatientModel import tbl_patient_disease,tbl_patient_information
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from HospitalSite.settings import LOGIN_REDIRECT_URL
import  datetime



@login_required(login_url= LOGIN_REDIRECT_URL)
def Add_Disease(request):        
    if request.method == "POST":
        AadhaarID = request.POST.get('AadhaarId')
        AadhaarID =AadhaarID.replace('-', '')
        pname = request.POST.get('pname')
        phone = request.POST.get('phone')
        AddedBy = request.session['loggedin_user']  
        type = request.POST.get('Dtype')
        fees = request.POST.get('fees')
        reportdate = request.POST.get('rdate')
        mediclaim = request.POST.get('mediclaim')
        drugs_prescribed = request.POST.get('drugs')
        otherdetails = request.POST.get('otherdata')

        if tbl_patient_information.objects.filter(AadhaarId=AadhaarID).first():
            disease_obj = tbl_patient_disease.objects.create( AadhaarId = AadhaarID,
            PatientName =pname,PatientNumber =  phone,DiseaseType = type,ReportDateTime = reportdate,FeesCharged=fees,MediclaimRaised = mediclaim,
            DrugsPrescribed =drugs_prescribed,    OtherDetails = otherdetails,AddedBy = AddedBy,created_at= datetime.datetime.now())
            disease_obj.save()
            messages.success(request, "Data Added Successfully")
               
            return render(request, 'dashboard/patient-disease.html')
               
        else:
            messages.warning(request, 'Please add Patient personal information')
            return redirect('/personal-info')
          
        
    return render(request, 'dashboard/patient-disease.html')



@login_required(login_url= LOGIN_REDIRECT_URL)
def SearchData(request):        

    if request.method == "POST":
        AadhaarID = request.POST.get('AadhaarId')
        AadhaarID =AadhaarID.replace('-', '')
        
        if tbl_patient_information.objects.filter(AadhaarId=AadhaarID).first():
            patient_info_obj = tbl_patient_information.objects.filter(AadhaarId=AadhaarID).values()
            patient_disease = tbl_patient_disease.objects.filter(AadhaarId=AadhaarID).values().all()
            context = {
                'personaldata': patient_info_obj,
                'diseasedata': patient_disease
                }
            return render(request, 'dashboard/view-data.html',context)
               
        else:
            messages.warning(request, 'Patient not found')
            return redirect('/search-data')
          
    
    return render(request, 'dashboard/search-data.html')
 


@login_required(login_url= LOGIN_REDIRECT_URL)
def ViewData(request):        
    return render(request, 'dashboard/view-data.html')



@login_required(login_url= LOGIN_REDIRECT_URL)
def ViewPersonalData(request,pk):     
    patient_info_obj = tbl_patient_information.objects.filter(AadhaarId=pk).values()
    patient_disease = tbl_patient_disease.objects.filter(AadhaarId=pk).values().all()
    context = {
        'personaldata': patient_info_obj,
        'diseasedata': patient_disease
        
    }   
    
    return render(request, 'dashboard/view-personal-data.html',context)



@login_required(login_url= LOGIN_REDIRECT_URL)
def ViewDiseaseData(request,pk):     
    patient_info_obj = tbl_patient_information.objects.filter(AadhaarId=pk).values()
    patient_disease = tbl_patient_disease.objects.filter(AadhaarId=pk).values().all()
    context = {
       'personaldata': patient_info_obj,
        'diseasedata': patient_disease
        
    }   
   
    
    return render(request, 'dashboard/patient-disease-data.html',context)