from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('api/add_water/', views.add_water_api, name='add_water_api'),
]
