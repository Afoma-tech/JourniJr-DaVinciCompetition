from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("registration/", views.kidregpage, name="kidreg"),
    path("travelkit/", views.travelpack, name='travelpack'),
    path("dashboard/", views.dashpage, name='dashpage'),
    path('login/', views.loginpage, name='loginpage'),

    path('generate-kit/',views.generate_packaging_kit, name='generate_packaging_kit'),
    path('chat/', views.chat_with_bot, name='chat_with_bot'),  # Add this line
    path('doctor/', views.doctor_view, name='doctor'),


]