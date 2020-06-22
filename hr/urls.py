from django.contrib import admin
from django.urls import path

from hr import views

urlpatterns = [
    path('', views.home, name='index'),
    path('acc', views.login, name='login'),
    path('acc/approve/<int:pk>', views.approve, name='approve'),
    path('applicant', views.applicant, name='applicant')
]
