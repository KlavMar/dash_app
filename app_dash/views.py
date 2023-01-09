
from django.http import HttpRequest
from django.shortcuts import render
from django_plotly_dash import DjangoDash
from django.conf import settings


def view_index(request):
    return render(request,"dashboard.html")
# Create your views here.
