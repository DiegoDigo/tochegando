# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 14:53
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='image',
            field=cloudinary.models.CloudinaryField(default=14, max_length=255, verbose_name='imagem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='image',
            field=cloudinary.models.CloudinaryField(default=11, max_length=255, verbose_name='imagem'),
            preserve_default=False,
        ),
    ]
