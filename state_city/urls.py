from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('addcity/', views.AddCity),
    path('addstate/',views.AddState),
    path('cities/<int:pk>/',views.DisplayCities),
    path('states/',views.DisplayStates)
]

