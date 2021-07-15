from django.contrib import admin
from app import views

urlpatterns = [    
    path('',          views.home,  name = 'home'),
    path('login/',    views.login, name = 'login'),
    path('register/', views.login, name = 'register')
]
