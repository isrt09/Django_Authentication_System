from django.contrib import admin
from app import views

urlpatterns = [    
    path('', views.home, name = 'home')
]
