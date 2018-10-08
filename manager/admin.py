# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Client, ClientVehicle, Brand, Kind,Vehicle,State,Country,City

admin.site.register(Client)
admin.site.register(ClientVehicle)
admin.site.register(Brand)
admin.site.register(Kind)
admin.site.register(Vehicle)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(City)
