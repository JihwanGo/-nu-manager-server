# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-04 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20171228_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='주소'),
        ),
    ]
