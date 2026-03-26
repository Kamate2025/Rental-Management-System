"""
URL configuration for rental_system_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('learn/', views.learn, name='learn'), #Remove this on deployment
    # path('login/', views.login, name='login'), #Pushed to user_management app
    path('user_management/', include('user_management.urls')),
    path('about_us/', views.about_us, name='about_us'),
    path('settings/', views.settings, name='settings'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_overview/', views.dashboard_overview, name='dashboard_overview'),
    path('properties/', include('properties.urls')),
    path('agents/', include('agents.urls')),
    path('payments/', include('payments.urls')),
    path('summary_report/', include('summary_report.urls')),
]
