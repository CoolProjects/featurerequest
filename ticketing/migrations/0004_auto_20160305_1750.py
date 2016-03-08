# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0003_featurerequest_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurerequest',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='ticketing.Client'),
        ),
    ]
