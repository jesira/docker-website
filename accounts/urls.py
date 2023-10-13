from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
  
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name= 'forgotPassword'),
    path('resetpassword_validate/<slug:uidb64>/<slug:token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name= 'resetPassword'),
   

]