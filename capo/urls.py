from django.urls import path

from . import views

urlpatterns = [

    path("Index", views.Index, name="Index"),
    path("Guitars",views.Guitars, name="Guitars"),
    path("Accessories",views.Accessoriess, name="Accessoriess"),
    path("Apparel",views.Apparels, name="Apparels")

    ]