# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-06 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0008_auto_20160305_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurerequest',
            name='title',
            field=models.CharField(help_text='Enter a short, descriptive name of the feature request.', max_length=300),
        ),
        migrations.AlterUniqueTogether(
            name='featurerequest',
            unique_together=set([('title', 'client')]),
        ),
    ]
