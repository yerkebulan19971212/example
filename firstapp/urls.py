from django.contrib import admin
from django.urls import path

from firstapp.views import get_html

urlpatterns = [
    path('firstapp/', get_html),
]
