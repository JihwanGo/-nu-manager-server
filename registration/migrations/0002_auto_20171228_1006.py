# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-28 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자', 'verbose_name_plural': '전체 사용자'},
        ),
        migrations.AddField(
            model_name='child',
            name='gender',
            field=models.CharField(choices=[('M', '남'), ('F', '여')], default='M', max_length=1, verbose_name='성별'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='profile_photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
