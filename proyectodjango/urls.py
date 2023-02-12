"""proyectodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('hello/',include("hello.urls"),name='hello'),
    path('newyear/',include("newyear.urls"),name='newyear'),
    path('task/',include("task.urls"),name='task'),
    path('pokemon/',include("pokemon.urls"),name='pokemon'),
    path('polls/',include("polls.urls"),name='polls'),
    path('admin/', admin.site.urls,name='admin'),
]
