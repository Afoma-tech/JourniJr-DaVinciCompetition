from django.shortcuts import render
from .forms import kidregform

# Create your views here.

def homepage(request):
    return render(request, 'index.html')


def kidregpage(request):
    form = kidregform()
    return render(request, 'kid_registration.html', {'form': form})

def travelpack(request):
    return render(request, 'travelkit1.html')