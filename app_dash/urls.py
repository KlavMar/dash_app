from django.shortcuts import render
from django.urls import path
from app_dash import views
from app_dash.dashboard import single_plot,first_subplot,dashboard_callback

urlpatterns = [
    path("", views.view_first_plot, name="first_plot"),
    path("dashboard/",views.first_dashboard,name="first_dashboard"),
    path("dashboard/call_back/",views.dashboard_callback,name="dashboard_callback")
    
]