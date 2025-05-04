from django.urls import path
from django.contrib import admin
from marks_list.views import search_student
from marks_list.views import home





urlpatterns = [
    
    path('',home,name='home'),
    path('search',search_student,name='src'),
   
 
    
]
