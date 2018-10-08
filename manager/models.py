# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.db import models

# class State(models.Model):

#     name = models.CharField(max_length=10)

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

# class Client(models.Model):
    
#     email = models.EmailField(max_length=254, unique=True)
#     identification = models.CharField(max_length=20, unique=True)
#     scanned_identification =models.FileField(upload_to='uploads/%Y/%m/%d/',default='scanned/default.jpg')

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

#     def __str__(self):
#         return self.first_name

# class Brand(models.Model):

#     name = models.CharField(max_length=70,unique=True)
#     image = models.ImageField(upload_to = 'brands/', default = 'brands/None/no-img.jpg')

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

#     def __str__(self):
#         return self.name

# class Country(models.Model):

#     name = models.CharField(max_length=70,unique=True)

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

#     def __str__(self):
#         return self.name

# class City(models.Model):

#     name = models.CharField(max_length=70,unique=True)
#     country = models.ForeignKey(Country,on_delete=models.CASCADE)

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

#     def __str__(self):
#         return self.name

# class Kind(models.Model):

#     name = models.CharField(max_length=70,unique=True)
#     image = models.ImageField(upload_to = 'kinds/', default = 'kinds/None/no-img.jpg')

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

#     def __str__(self):
#         return self.name

# class Vehicle(models.Model):
    
#     enrollment = models.CharField(max_length=10)
#     city = models.ForeignKey(City,on_delete=models.CASCADE, default=1)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     kind = models.ForeignKey(Kind, on_delete=models.CASCADE)

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

#     class Meta:
#         unique_together = (("brand", "city"),)

#     def __str__(self):
#         return self.enrollment

# class ClientVehicle(models.Model):

#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     state= models.ForeignKey(State,on_delete=models.CASCADE,default=1)

#     def __str__(self):
#         return self.user.first_name