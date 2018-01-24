# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-19 00:47
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(max_length=50, verbose_name='이름')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=100, verbose_name='주소')),
                ('parent_relationship', models.CharField(choices=[('F', '아버지'), ('M', '어머니'), ('GF', '할아버지'), ('GM', '할머니'), ('O', '기타')], max_length=2, verbose_name='관계')),
                ('parent_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='휴대폰 번호')),
            ],
            options={
                'verbose_name': '학생',
                'verbose_name_plural': '학생',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
            ],
            options={
                'verbose_name': '반',
                'verbose_name_plural': '반',
            },
        ),
        migrations.CreateModel(
            name='Preschool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('region', models.CharField(choices=[('SE', '서울'), ('BS', '부산'), ('DG', '대구'), ('IC', '인천'), ('GJ', '광주'), ('DJ', '대전'), ('US', '울산'), ('SJ', '세종'), ('GG', '경기'), ('GW', '강원'), ('CB', '충북'), ('CN', '충남'), ('JB', '전북'), ('JN', '전남'), ('GB', '경북'), ('GN', '경남'), ('JJ', '제주')], max_length=2, verbose_name='지역')),
            ],
            options={
                'verbose_name': '유치원',
                'verbose_name_plural': '유치원',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '선생님',
                'verbose_name_plural': '선생님',
            },
            bases=('registration.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='preschool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='registration.Preschool', verbose_name='소속 유치원'),
        ),
        migrations.AddField(
            model_name='child',
            name='assigned_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='registration.Class', verbose_name='반'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='assigned_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='registration.Class', verbose_name='반'),
        ),
    ]
