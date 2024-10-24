from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def kidregpage(request):
    return render(request, 'kid_registration.html')