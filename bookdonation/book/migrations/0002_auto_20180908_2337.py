# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-08 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]