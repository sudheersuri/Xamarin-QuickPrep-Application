from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addform/getq', views.displayques ,name='displayques'),
    path('login/', views.login ,name='login'),
    path('login/checklogin', views.checklogin ,name='checklogin'),
    path('addsub/', views.addsubname ,name='addsubname'),
    path('add/', views.addtodb ,name='add'),
    path('allsubjects/',views.allsubjects,name='allsubjectss'),
    path('editor/',views.editor,name='editor'),
    path('subeditor/',views.subeditor,name='subeditor'),
    path('editquestion/',views.editquestion,name='editquestion'),
    path('editsubject/',views.editsubject,name='editsubject'),
]