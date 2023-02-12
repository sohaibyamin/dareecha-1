from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


# Create your views here.
def view_index(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))
