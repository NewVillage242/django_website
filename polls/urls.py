from django.urls import path

from . import views

urlpatterns = [
    path("", views.json, name="json"),
    path("index", views.index, name="index"),
    path("no_index", views.no_index, name="no_index"),
]