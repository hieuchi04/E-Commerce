from django.conf import settings
from django.db import models

from apps.product.models import Product

User = settings.AUTH_USER_MODEL

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=0)


class CartItem(models.Model): 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    count = models.IntegerField(default=0)
