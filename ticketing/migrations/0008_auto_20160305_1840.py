# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0007_auto_20160305_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurerequest',
            name='priority',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
