# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-03 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cQuiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='c_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='q_id',
            field=models.IntegerField(default=0),
        ),
    ]
