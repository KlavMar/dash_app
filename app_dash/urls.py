from django.shortcuts import render
from django.urls import path
from app_dash import views
from app_dash.dashboard import single_plot

urlpatterns = [
    path("dashboard/", views.view_index, name="view_index"),
    
]