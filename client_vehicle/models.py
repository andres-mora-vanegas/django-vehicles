from django.db import models
from client.models import Client
from vehicle.models import Vehicle
from state.models import State

# Create your models here.
class ClientVehicle(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.client.first_name