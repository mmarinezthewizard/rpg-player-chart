from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerChartView.get_chart,name='index'),
    path('playerindex/', views.PlayerChartView.get_player_stats),
    path('playerindex/deletePlayer/<int:player>/', views.PlayerChartView.delete_player)
]
