from django.db import models
from state.models import State

# Create your models here.
class VehicleKind(models.Model):
    
    name = models.CharField(max_length=70,unique=True)
    image = models.ImageField(upload_to = 'kinds/', default = 'kinds/None/no-img.jpg')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name