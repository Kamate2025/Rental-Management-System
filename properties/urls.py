from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties_list, name='properties_list'),
    
    # Property Types
    path('add_type/', views.add_property_type, name='add_property_type'),
    path('add_type/cancel/', views.add_property_cancel, name='add_property_cancel'),
    path('type/edit/<int:pk>/', views.edit_property_type, name='edit_property_type'),
    path('type/view/<int:pk>', views.view_property_type, name='view_property_type'),
    path('type/<int:pk>/delete/', views.delete_property_type, name='delete_property_type'),
    
    # Properties
    path('add_property', views.add_property, name='add_property'),
    path('delete/<int:pk>/', views.delete_property, name='delete_property'),
    path('view/<int:pk>/', views.view_property, name='view_property'),
    path('edit/<int:pk>/', views.edit_property, name='edit_property'),
]
