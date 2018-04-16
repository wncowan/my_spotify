# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(max_length=255, unique=True)),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
                ('liked_others', models.ManyToManyField(related_name='otherlikedsongs', to='login_registration.User')),
            ],
        ),
    ]