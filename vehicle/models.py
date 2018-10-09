from django.db import models

from city.models import City
from brand.models import Brand
from vehicle_kind.models import VehicleKind
from state.models import State

# Create your models here.
class Vehicle(models.Model):

    enrollment = models.CharField(max_length=10)
    city = models.ForeignKey(City,on_delete=models.CASCADE, default=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='brands')
    kind = models.ForeignKey(VehicleKind, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

    class Meta:
        unique_together = (("enrollment", "city"),)

    def __str__(self):
        return self.enrollment