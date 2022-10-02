from django.urls import path, include
from . import views

urlpatterns = [
    path('posting/', views.posting),
]