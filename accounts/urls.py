from django.urls import path
from .import views
from django.conf.urls import url, include

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout')
]