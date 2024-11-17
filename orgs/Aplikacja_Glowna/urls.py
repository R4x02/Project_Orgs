from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.main, name='main'),  # Główna strona
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('join-team/', views.join_team, name='join_team'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('add-team/', views.add_team, name='add_team'),
    path('accounts/profile/', views.profile_redirect, name='profile_redirect'),
]
