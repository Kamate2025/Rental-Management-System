from django.urls import path
from . import views


urlpatterns = [
    path('', views.agents_list, name='agents_list')
]
