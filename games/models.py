from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    release_date = models.DateField()
    developer = models.CharField(max_length=255)

    # НОВІ ПОЛЯ:
    category = models.CharField(max_length=100, default="General")
    image = models.ImageField(upload_to='games_images/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title