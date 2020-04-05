from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addform/getqform', views.displaysubform ,name='displaysubform'),
    path('addform/getq', views.displayques ,name='displayques'),
    path('login/', views.login ,name='login'),
    path('login/checklogin', views.checklogin ,name='checklogin'),
    path('addsub/', views.addsubname ,name='addsubname'),
    path('add/', views.addtodb ,name='add'),
    path('allsubjects/',views.allsubjects,name='allsubjectss')
]