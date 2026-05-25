from django.urls import path
from .views import home, landing
from . import views

urlpatterns = [
    path('', landing, name='landing'),
    path('home/', home, name='home'),
path('add-game/', views.add_game, name='add_game')
]