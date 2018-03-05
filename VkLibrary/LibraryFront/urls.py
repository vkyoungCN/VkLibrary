'''
Created on 2018年3月5日

@author: VkYoung16
'''

from django.urls import path 
from . import views

urlpatterns = [
    path('index/',views.index), 
    path('',views.index)
]