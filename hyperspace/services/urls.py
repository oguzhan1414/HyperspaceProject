from django.urls import path
from . import views

urlpatterns = [
    path('',views.service_list, name='service_list'),
    path('<slug:slug>/', views.service_details, name='service_details'),  #slug yapılı bir slug göndericez 
]
