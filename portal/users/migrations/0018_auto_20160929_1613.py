# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-29 16:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20160929_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name_plural': 'locations'},
        ),
    ]
