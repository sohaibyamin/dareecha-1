from django.urls import path
from baham import views

urlpatterns = [
    path('', views.view_index, name='home')
]
