# core/urls.py - OLMASI GEREKEN TEMİZ HALİ

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('portal/', views.portal_view, name='portal'),
    path('firms/', views.firm_list_view, name='firm-list'),
    path('firms/add/', views.firm_create_view, name='firm-add'),
    path('firms/edit/<int:pk>/', views.firm_update_view, name='firm-update'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('firms/delete/<int:pk>/', views.firm_delete_view, name='firm-delete'),
]