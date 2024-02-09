from django.urls import path
from . import views
# from .views import add_lead
from .views import AddLeadView

urlpatterns = [
    path('', views.leads_list, name='leads_list'),
    path('<int:pk>/', views.leads_detail, name='leads_detail'),
     path('add_lead/', AddLeadView.as_view(), name='add_lead'),
]