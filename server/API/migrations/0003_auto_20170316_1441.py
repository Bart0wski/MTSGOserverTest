# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='rightAnswer',
            field=models.CharField(choices=[('1', models.CharField(max_length=20)), ('2', models.CharField(max_length=20)), ('3', models.CharField(max_length=20)), ('4', models.CharField(max_length=20))], max_length=20),
        ),
    ]