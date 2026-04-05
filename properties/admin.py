from django.contrib import admin
from .models import PropertyType, PropertyRegistration, PropertyOwnership


class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    
class PropertyRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'property_type', 'location', 'price', 'owner', 'agent', 'status', 'contact')

admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(PropertyRegistration, PropertyRegistrationAdmin)
admin.site.register(PropertyOwnership)
