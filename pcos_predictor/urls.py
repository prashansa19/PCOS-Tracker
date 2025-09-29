"""
URL configuration for pcos_predictor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from predictor.views import home_page,general_create_view,medical_create_view,result_view, register, login, logout, history, start_page, edit_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name='home'),
    path('', start_page, name='start'),
    path('general/', general_create_view, name='general_create_view'),
    path('medical/', medical_create_view, name='medical_create_view'),
    path('result/<int:pk>/', result_view, name='result_view'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('history/', history, name='history'),
    path('edit/<str:type>/<int:pk>/', edit_view, name='edit_view'),
]
