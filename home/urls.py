from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("signup",views.handleSignUp, name='handleSignUp'),
    path("login",views.handleLogin, name='handleLogin'),
    path("logout",views.handleLogout, name='handleLogout')
]
