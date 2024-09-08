from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()

    def is_available(self):
        return self.stock > 5
    
    def name_of_product(self):
        return self.name
    
    def is_good(self):
        return self.rating>3