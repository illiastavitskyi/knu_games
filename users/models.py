from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    country = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Game(models.Model):
        title = models.CharField(max_length=255)
        description = models.TextField()

        price = models.DecimalField(max_digits=8, decimal_places=2)

        release_date = models.DateField()

        developer = models.CharField(max_length=255)

        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.game.title} ({self.price})"
