# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-10 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20181010_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='state.State'),
        ),
    ]
