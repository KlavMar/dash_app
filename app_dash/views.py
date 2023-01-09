
from django.http import HttpRequest
from django.shortcuts import render
from django_plotly_dash import DjangoDash
from django.conf import settings


def view_first_plot(request):
    return render(request,"first_plot.html")
# Create your views here.

def first_dashboard(request):
    return render(request,"first_dashboard.html")


def dashboard_callback(request):
    return render(request,"dashboard_callback.html")