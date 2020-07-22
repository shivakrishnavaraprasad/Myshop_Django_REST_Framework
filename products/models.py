from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50,
                             default='')
    price = models.IntegerField() 
    rating = models.CharField(max_length=10, 
                              default='')

    def __str__(self):
        return self.name

