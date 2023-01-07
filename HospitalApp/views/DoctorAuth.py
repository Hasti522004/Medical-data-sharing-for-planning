from datetime import date
from xmlrpc.client import DateTime
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
#from HospitalApp.models.HospitalAuthModel import *
from django.contrib import messages

from HospitalApp.models.HospitalAuthModel import tbl_doctor_register, tbl_hospital_register
from django.contrib.auth import authenticate, logout, login as auth_login
from HospitalSite.settings import LOGIN_REDIRECT_URL

def Doctor_login(request):  

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        try:
            email = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, "User not found")
            return redirect("/doctor-login")

        user_obj = User.objects.filter(username=email).first()

        if user_obj is None:
            messages.warning(request, "User not found")
            return redirect("/doctor-login")

        profile_obj = tbl_doctor_register.objects.filter(user=user_obj).first()
        user = authenticate(username=email, password=password)
        if user is None:
            messages.warning(request, "Invalid Email Or Password")
            return redirect("/doctor-login")
        else:

            auth_login(request, user)
            current_user = request.user
            doctor_id = profile_obj.DoctorID
            request.session['loggedin_user'] = doctor_id
    
            return redirect("/dashboard")
    
    return render(request, 'doctor-auth/doctor-auth-login.html')


def Doctor_register(request):     
    if request.method == "POST":
        #id = request.POST.get('hospitalID')
        name = request.POST.get('doctorname')
        email = request.POST.get('email')
        number = request.POST.get('number')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        education = request.POST.get('education')
        password = request.POST.get('password')

        try:
            if User.objects.filter(email=email).first():
                messages.warning(request, 'User already exits!')
                return redirect('/doctor-register')
            if tbl_doctor_register.objects.filter(email=email).first():
                messages.warning(request, 'Email already taken!')
                return redirect('/doctor-register')

            user_obj = User.objects.create_user(username=name, email=email, password=password)
           
            Doctor_login_obj = tbl_doctor_register.objects.create(user=user_obj,name=name, email=email, number=number,gender=gender,address=address,education=education)
            user_obj.save()
            Doctor_login_obj.save()
            messages.success(request, "Account created successfully")
        except Exception as e:
            print(e)
            return redirect('/error')
        
    return render(request, 'doctor-auth/doctor-auth-register.html')



