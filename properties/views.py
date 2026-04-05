from django.shortcuts import render
from . models import PropertyType, PropertyRegistration



def properties_list(request):
    property_type = PropertyType.objects.all()
    properties = PropertyRegistration.objects.all()
    context = {
        'property_type': property_type,
        'properties': properties,
    }
    return render(request, 'properties/property_list.html', context)
