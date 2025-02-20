from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('timer/', views.countdown_timer, name='countdown_timer'),
]