from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('join-team/', views.join_team, name='join_team'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('add-team/', views.add_team, name='add_team'),
]