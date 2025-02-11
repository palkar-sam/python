from django.urls import path;
from hello import views;

urlpatterns = [
    path("", views.Home, name="home"),
    #path("hello/<name>", views.HelloThere, name="HelloThere"),
    path("hello/<name>", views.HelloDispatch, name="HelloDispatch"),
    path("hello/<name>/func1", views.HelloThere, name="HelloThere"),
    path("hello/<name>/func2", views.HelloTemplate, name="HelloTemplate"),
]