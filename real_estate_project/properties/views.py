from django.shortcuts import render, get_object_or_404
from .models import Property

def home(request):
    properties = Property.objects.all()

    location = request.GET.get('location')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if location:
        properties = properties.filter(location__icontains=location)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)

    return render(request, 'properties/home.html', {'properties': properties})



def search(request):
    query = request.GET.get('q')
    if query:
        properties = Property.objects.filter(title__icontains=query)
    else:
        properties = Property.objects.all()
    return render(request, 'properties/search_results.html', {'properties': properties})



def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'properties/property_detail.html', {'property': property})