from django.shortcuts import get_object_or_404, render, redirect

from .forms import PropertyTypeForm, PropertyRegistrationForm
from . models import PropertyType, PropertyRegistration



def properties_list(request):
    property_type = PropertyType.objects.all()
    properties = PropertyRegistration.objects.all()
    count = properties.count()
    context = {
        'property_type': property_type,
        'properties': properties,
        'count': count,
    }
    return render(request, 'properties/property_list.html', context)

def add_property_type(request):
    if request.method == 'POST':
        form = PropertyTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('properties_list')
    form = PropertyTypeForm()
    context = {
        'form': form,
    }
    return render(request, 'properties/add_property_type.html', context)


def add_property_cancel(request):
    return redirect('properties_list')

def edit_property_type(request, pk):
    p_type = get_object_or_404(PropertyType, pk=pk)
    if request.method == 'POST':
        edit_form = PropertyTypeForm(request.POST, instance=p_type)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('properties_list')
    edit_form = PropertyTypeForm(instance=p_type)
    context = {
        'p_type': p_type,
        'edit_form': edit_form,
    }
    return render(request, 'properties/edit_property_type.html', context)

def view_property_type(request, pk):
    p_type = get_object_or_404(PropertyType, pk=pk)
    context = {
        'p_type': p_type,
    }
    return render(request, 'properties/view_property_type.html', context)


def delete_property_type(request, pk):
    p_type = get_object_or_404(PropertyType, pk=pk)
    p_type.delete()
    return redirect('properties_list')

def add_property(request):
    if request.method == "POST":
        reg_form = PropertyRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('properties_list')
    reg_form = PropertyRegistrationForm()
    context = {
        'reg_form': reg_form,
    }
    return render(request, 'properties/add_property.html', context)

def delete_property(request, pk):
    property = get_object_or_404(PropertyRegistration, pk=pk)
    property.delete()
    return redirect('properties_list')

def view_property(request, pk):
    property = get_object_or_404(PropertyRegistration, pk=pk)
    context = {
        'property': property,
    }
    return render(request, 'properties/view_property.html', context)

def edit_property(request, pk):
    property = get_object_or_404(PropertyRegistration, pk=pk)
    if request.method == 'POST':
        edit_form = PropertyRegistrationForm(request.POST, instance=property)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('properties_list')
    edit_form = PropertyRegistrationForm(instance=property)
    context = {
        'edit_form': edit_form,
        'property': property,
    }
    return render(request, 'properties/edit_property.html', context)
