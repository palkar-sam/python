from django.urls import path;
from hello import views;

urlpatterns = [
    path("", views.Home, name="home"),
]