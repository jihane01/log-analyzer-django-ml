# analyzer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_log, name='analyze_log'),
]