from datetime import date
from xmlrpc.client import DateTime
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
#from HospitalApp.models.HospitalAuthModel import *
from django.contrib import messages

from HospitalApp.models.HospitalAuthModel import tbl_hospital_register
from django.contrib.auth import authenticate, logout, login as auth_login
from HospitalSite.settings import LOGIN_REDIRECT_URL

def Hospital_login(request):    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        try:
            email = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, "User not found")
            return redirect("/hospital-login")

        user_obj = User.objects.filter(username=email).first()

        if user_obj is None:
            messages.warning(request, "User not found")
            return redirect("/hospital-login")

        profile_obj = tbl_hospital_register.objects.filter(user=user_obj).first()
        user = authenticate(username=email, password=password)
        if user is None:
            messages.warning(request, "Invalid Email Or Password")
            return redirect("/hospital-login")
        else:
            auth_login(request, user)
            current_user = request.user
            hospital_id = profile_obj.id
            request.session['loggedin_user'] = hospital_id 
    
            return redirect("/dashboard")
    return render(request, 'hospital-auth/hospital-auth-login.html')


def Hospital_register(request):        
    if request.method == "POST":
        id = request.POST.get('hospitalID')
        name = request.POST.get('hospitalName')
        email = request.POST.get('email')
        number = request.POST.get('number')
        type = request.POST.get('type')
        address = request.POST.get('address')
        doctorname = request.POST.get('doctorName')
        password = request.POST.get('password')

        try:
            if User.objects.filter(email=email).first():
                messages.warning(request, 'User already exits!')
                return redirect('/hospital-register')
            if tbl_hospital_register.objects.filter(email=email).first():
                messages.warning(request, 'Email already taken!')
                return redirect('/hospital-register')

            user_obj = User.objects.create_user(username=name, email=email, password=password)
           
            Hospital_login_obj = tbl_hospital_register.objects.create(user=user_obj,id=id,name=name, email=email, number=number,type=type,address=address,doctor_name=doctorname)
            user_obj.save()
            Hospital_login_obj.save()
            messages.success(request, "Account created successfully")
        except Exception as e:
            print(e)
            return redirect('/error')
    return render(request, 'hospital-auth/hospital-auth-register.html')







def logoutUser(requests):
    requests.session.clear()
    logout(requests)
    messages.success(requests, 'Logged out successfully')
    return redirect('/')