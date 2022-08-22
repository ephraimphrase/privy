from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('room/<str:pk>/', views.room, name='room'),
    path('checkRoom', views.checkRoom, name='checkRoom'),
    path('send', views.send, name='send'),
    path('getMessages/<str:pk>/', views.getMessages, name='getMessages')
]
