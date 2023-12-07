
from django.urls import path

from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.home, name="index"),
    path("crearClientesVarios/", views.crearClientesVarios),
    path("busqueda/", views.busqueda),
    path("crear/", views.crear),
    path("/", views.crear),
]