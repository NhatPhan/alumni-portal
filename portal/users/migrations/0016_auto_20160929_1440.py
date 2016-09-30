# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-29 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_pointofinterest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('position', geoposition.fields.GeopositionField(blank=True, max_length=42)),
            ],
            options={
                'verbose_name_plural': 'points of interest',
            },
        ),
        migrations.DeleteModel(
            name='PointOfInterest',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
    ]