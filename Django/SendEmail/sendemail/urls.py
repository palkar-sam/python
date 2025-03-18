from django.urls import path
from sendemail import views


urlpatterns =[
    path('', views.index, name='index'),
]