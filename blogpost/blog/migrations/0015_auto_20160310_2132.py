# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-10 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_meansize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meansize',
            name='movie_id',
            field=models.IntegerField(default=0),
        ),
    ]
