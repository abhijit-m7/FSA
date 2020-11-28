from django.contrib import admin 
from django.urls import path 

from . import views
urlpatterns = [
    path('', views.loginPage , name = 'login'),
    path('contact/', views.ContactPage , name = 'contact'),
    path('login/', views.logOutPage , name = 'logout'),
    path('Analytics/', views.Analytics , name = 'Analytics'),
    
]