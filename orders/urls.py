from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.view_cart, name='cart'),                           # Сторінка кошика
    path('add-to-cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'), # Функція додавання у кошик
    path('checkout/', views.checkout, name='checkout'),                    # Функція списання коштів
]