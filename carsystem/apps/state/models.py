from django.db import models

# Create your models here.
class State(models.Model):

    name = models.CharField(max_length=10)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name