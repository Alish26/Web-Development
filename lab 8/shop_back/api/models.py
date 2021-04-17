from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    descritption = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()

    def to_json(self):
        return {
            'id': self.id,
            'price': self.price,
            'description': self.descritption,
            'count': self.count,
            'is_active': self.is_active
        }

class Category(models.Model):
    name = models.TextField()

    def to_json(self):
        return {
            'name': self.name
        }
