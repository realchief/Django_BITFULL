# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170827_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountNameOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('account_name', models.CharField(max_length=100)),
            ],
        ),
    ]