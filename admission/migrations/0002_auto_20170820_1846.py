# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='Registree',
            new_name='registree',
        ),
        migrations.AlterField(
            model_name='admission',
            name='student_card_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registration',
            name='registration_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]