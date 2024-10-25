from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("registration/", views.kidregpage, name="kidreg"),
    path("travelkit/", views.travelpack, name='travelpack'),
    path("dashboard/", views.dashpage, name='dashpage'),
    path('login/', views.loginpage, name='loginpage'),
]