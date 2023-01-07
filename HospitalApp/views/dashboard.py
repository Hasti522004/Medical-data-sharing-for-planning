from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from HospitalSite.settings import LOGIN_REDIRECT_URL


@login_required(login_url= LOGIN_REDIRECT_URL)
def dash_index(request):        
    return render(request, 'dashboard/dashboard.html')


def error(request):
    return render(request, "dashboard/error.html")