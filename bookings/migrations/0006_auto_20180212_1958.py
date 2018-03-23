# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-12 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20180212_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingavailability',
            name='account_social',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='availability_prefs', to='socialaccount.SocialAccount'),
        ),
    ]