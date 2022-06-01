from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=140)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[
                                 MinValueValidator(0.00), MaxValueValidator(5.00)])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(5)])
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="reviews")

    def __str__(self):
        return str(self.rating)
