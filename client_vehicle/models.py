from django.db import models
from Client.models import Client
from Vehicle.models import Vehicle
from State.models import State

# Create your models here.
class ClientVehicle(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.user.first_name