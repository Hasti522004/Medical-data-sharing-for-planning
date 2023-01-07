from django.shortcuts import redirect, render


def index(request):        
    return render(request, 'landing-pages/index.html')




def schemes(request):        
    return render(request, 'schemes/schemes.html')