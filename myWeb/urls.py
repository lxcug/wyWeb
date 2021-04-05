"""myWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from firstweb import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles


urlpatterns = [
    path('admin/', admin.site.urls, name='main'),
    path('index/', views.index, name='index'),
    path('plot/', views.getPlotData, name='getPlotData'),
    path('ansP', views.plot, name='plot'),
    path('scatter/', views.getScatterData, name='getScatterData'),
    path('ansS', views.scatter, name='scatter'),
    path('polyfit/', views.getPolyFitData, name='getPolyData'),
    path('ansPoly', views.polyFit, name='polyFit')
]



urlpatterns += staticfiles_urlpatterns()
