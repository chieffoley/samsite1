# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_auto_20160524_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='acquired_date',
            field=models.DateTimeField(verbose_name='date acquired'),
        ),
    ]