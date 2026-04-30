from django.contrib import admin
from .models import Profile, Game, Order, OrderItem

admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(Order)
admin.site.register(OrderItem)