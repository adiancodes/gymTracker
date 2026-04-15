from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('api/add_water/', views.add_water_api, name='add_water_api'),
    path('api/update_goal/', views.update_goal_api, name='update_goal_api'),
    path('delete_workout/<int:workout_id>/', views.delete_workout_view, name='delete_workout'),
    path('history/', views.history_view, name='history'),
]
