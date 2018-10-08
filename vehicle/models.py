from django.db import models

from City.model import City
from Brand.model import Brand
from Kind.model import Kind
from State.model import State

# Create your models here.
class Vehicle(models.Model):

    enrollment = models.CharField(max_length=10)
    city = models.ForeignKey(City,on_delete=models.CASCADE, default=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

    class Meta:
        unique_together = (("brand", "city"),)

    def __str__(self):
        return self.enrollment