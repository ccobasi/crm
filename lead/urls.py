from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.leads_list, name='leads_list'),
    path('<int:pk>/', views.leads_detail, name='leads_detail'),
    path('dashboard/leads/<int:pk>/delete/', leads_delete, name='leads_delete'),
    path('dashboard/leads/<int:pk>/edit/', leads_edit, name='leads_edit'),
    path('dashboard/leads/<int:pk>/convert/', convert_to_client, name='leads_convert'),
    path('add_lead/', AddLeadView.as_view(), name='add_lead'),
]