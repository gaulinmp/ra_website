# -*- coding: utf-8 -*-

from django.urls import path

from . import views

app_name="html_checker"
urlpatterns = [
    # View
    path('', views.view, name='index'),
    # API
    path('upload', views.upload, name='upload'),
    path('download', views.download, name='download'),
    path('add_note', views.add_note, name='add_note'),
]
