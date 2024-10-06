from django.shortcuts import render, get_object_or_404
from .models import Property

def home(request):
    properties = Property.objects.all()
    return render(request, 'properties/home.html', {'properties': properties})




def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'properties/property_detail.html', {'property': property})