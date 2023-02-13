from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from baham.enum_types import VehicleStatus
from baham.models import Vehicle, VehicleModel, UserProfile


# Create your views here.
def view_index(request):
    template = loader.get_template('home.html')
    # Fetch the last 20 records
    vehicles = Vehicle.objects.all().order_by('-vehicle_id').values()
    context = {
        "navbar": "home",
        "vehicles": vehicles
    }
    return HttpResponse(template.render(context, request))


def view_members(request):
    template = loader.get_template('members.html')
    context = {
        "navbar": "members"
    }
    return HttpResponse(template.render(context, request))


def view_vehicles(request):
    template = loader.get_template('vehicles.html')
    context = {
        "navbar": "vehicles"
    }
    return HttpResponse(template.render(context, request))


def create_vehicle(request):
    template = loader.get_template('createvehicle.html')
    models = VehicleModel.objects.all().values_list('model_id', 'vendor', 'model', 'type')
    users = User.objects.filter(is_superuser=False, is_active=True).all().values_list('id', 'first_name', 'last_name', 'email')
    context = {
        "navbar": "vehicles",
        "models": models,
        "users": users,
        "statuses": [e.value for e in VehicleStatus]
    }
    return HttpResponse(template.render(context, request))


def save_vehicle(request):
    registration_number = request.POST['registration_number']
    color = request.POST['color']
    model_id = request.POST['model_id']
    owner_id = request.POST['owner_id']
    status = request.POST['status']
    if not registration_number or not model_id or not owner_id:
        return HttpResponse('<h3 class="danger">Error! Required parameters are missing.<h3>')
    model = VehicleModel.objects.filter(pk=model_id).get()
    owner = UserProfile.objects.filter(pk=owner_id).get()
    obj = Vehicle(registration_number=registration_number, color=color, model=model,
                  owner=owner, status=status)
    obj.save()
    return HttpResponseRedirect(reverse('vehicles.html'))


def view_aboutus(request):
    template = loader.get_template('aboutus.html')
    context = {
        "navbar": "aboutus"
    }
    return HttpResponse(template.render(context, request))
