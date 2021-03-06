# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-22 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('normalization', '0005_auto_20170709_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transcription', models.CharField(max_length=30)),
                ('normalization', models.CharField(max_length=30)),
                ('lemma', models.CharField(max_length=30)),
                ('annotation', models.TextField()),
                ('translation', models.CharField(max_length=50)),
                ('to_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='normalization.Model')),
            ],
            options={
                'verbose_name_plural': 'Words normalized manually',
            },
        ),
    ]
