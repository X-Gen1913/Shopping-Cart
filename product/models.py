from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    seller= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    details= models.TextField()
    check=models.CharField(max_length=200)
    price = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
class OrderItem(models.Model):
    product=models.OneToOneField(Product,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.product.title



class Order(models.Model):
    buyer=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)


    def add(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return self.buyer

