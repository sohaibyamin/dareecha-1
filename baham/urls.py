from django.urls import path
from baham import views

urlpatterns = [
    path('', views.view_index, name='home'),
    path('baham/members/', views.view_members, name='members'),
    path('baham/vehicles/', views.view_vehicles, name='vehicles'),
    path('baham/vehicles/create/', views.create_vehicle, name='create_vehicle'),
    path('baham/vehicles/create/save/', views.save_vehicle, name='save_vehicle'),
    path('baham/aboutus/', views.view_aboutus, name='aboutus')
]
