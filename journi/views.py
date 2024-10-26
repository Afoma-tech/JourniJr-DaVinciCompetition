from django.shortcuts import render, redirect
from .forms import kidregform

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def kidregpage(request):
    form = kidregform()
    return render(request, 'kid_registration.html', {'form': form})

def travelpack(request):
    return render(request, 'travelkit1.html')

def dashpage(request):
    return render(request, 'dashboard.html')

def loginpage(request):
    if request.method == 'POST':
        return redirect('kid_registration.html')  

    return render(request, 'login.html')