# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-25 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160925_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dateofbirth',
            field=models.DateField(null=True),
        ),
    ]
