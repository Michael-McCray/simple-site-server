from django.db import models
from products.models import *
from users.models import *

class Order(models.Model):
    user_id = models.ForeignKey('users.Profile',on_delete=models.CASCADE, blank=True)
    product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    price = models.IntegerField()
    address = models.TextField(max_length=200,null=True)
    email = models.TextField(max_length=200,null=True)
    delivered = models.BooleanField(default=False)
    refund = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.email