# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),


    # re_path(r'^.*\.*', views.pages, name='pages'),

    path('charts', views.charts, name='charts'),
    path('incidentForm', views.incidentForm, name='incidentForm'),
    path('unassignedTask', views.taskUnassignedView, name='unassignedTask'),
    path('assigneeForm/<int:id>', views.assignFormView, name='assigneeForm'),
    path('allTask', views.allTaskView, name='allTask'),

]

