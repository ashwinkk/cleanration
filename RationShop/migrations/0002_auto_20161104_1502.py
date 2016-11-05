# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RationShop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complaint', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='Shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RationShop.RationShop'),
        ),
        migrations.AddField(
            model_name='complaintlog',
            name='RationId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RationShop.Customer'),
        ),
        migrations.AddField(
            model_name='complaintlog',
            name='Shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RationShop.RationShop'),
        ),
    ]