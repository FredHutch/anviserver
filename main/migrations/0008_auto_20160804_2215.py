# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 22:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160804_2214'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectSharedUser',
            new_name='ProjectUser',
        ),
    ]