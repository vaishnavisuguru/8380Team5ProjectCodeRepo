# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-26 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
