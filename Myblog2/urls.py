"""Myblog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name="login.html")),
    # path('register/',views.User_Register),
    path('',views.Home_Post),
    path('addpost/',views.Add_Post),
    path('editpost/<int:id>/',views.Edit_Post),
    path('showpost/',views.Show_Post),
    path('delete/<int:id>/', views.Delete_Post),
    path('logout/', auth_views.LogoutView.as_view()),


]
