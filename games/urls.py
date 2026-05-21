from django.urls import path
from .views import home, landing

urlpatterns = [
    path('', landing, name='landing'),
    path('home/', home, name='home'),
]