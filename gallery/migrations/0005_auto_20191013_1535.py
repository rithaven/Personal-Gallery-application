# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-13 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20191012_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Category_image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
    ]