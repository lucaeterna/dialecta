# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-03-04 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morphology', '0004_remove_dialect_model_to_normalize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dialect',
            name='abbreviation',
            field=models.CharField(max_length=10),
        ),
    ]
