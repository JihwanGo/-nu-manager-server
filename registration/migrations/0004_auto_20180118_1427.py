# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 05:27
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20180104_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='profile_photo',
            field=sorl.thumbnail.fields.ImageField(upload_to='profiles', verbose_name='프로필 사진'),
        ),
    ]
