from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('add-game/', views.add_game, name='add_game'),
path('game/<int:game_id>/', views.game_detail, name='game_detail'),
]