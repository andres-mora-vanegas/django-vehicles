from django.db import models
from Country.model import Country
from State.model import State
# Create your models here.

class City(models.Model):
    
    name = models.CharField(max_length=70,unique=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name