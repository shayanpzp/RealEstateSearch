from django.shortcuts import render
from .models import Property

def home(request):
    properties = Property.objects.all()
    return render(request, 'properties/home.html', {'properties': properties})
