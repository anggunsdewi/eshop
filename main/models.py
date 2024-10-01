import uuid
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    rating = models.FloatField()
    categories = models.ManyToManyField(Category, related_name='products')

    def name_of_product(self):
        return self.name
    
    def is_available(self):
        return self.stock > 0
    
    def is_good(self):
        return self.rating > 3