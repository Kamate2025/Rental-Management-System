from django.shortcuts import render

# Create your views here.
def properties_list(request):
    return render(request, 'properties/property_list.html')
