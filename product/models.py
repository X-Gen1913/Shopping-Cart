from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    seller= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    details= models.TextField()
    check=models.CharField(max_length=200)
    price = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
class Order(models.Model()):
    buyer=models.ForigenKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orderproduct=models.Manytomany()
