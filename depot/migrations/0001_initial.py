# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RationShop', '0003_auto_20161104_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField(default=False)),
                ('RationShop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RationShop.RationShop')),
            ],
        ),
    ]