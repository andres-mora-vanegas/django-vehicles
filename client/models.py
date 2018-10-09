from django.db import models
from state.models import State

# Create your models here.

class Client(models.Model):

    email = models.EmailField(max_length=254, unique=True)
    identification = models.CharField(max_length=20, unique=True)
    scanned_identification =models.FileField(upload_to='uploads/%Y/%m/%d/',default='scanned/default.jpg')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.first_name