# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-17 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, b'Design'), (2, b'Back-end'), (3, b'Front-end')], verbose_name=b'Category')),
                ('skill', models.CharField(max_length=100, verbose_name=b'Skill')),
                ('order', models.SmallIntegerField(verbose_name=b'Order on website')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-modified_date'],
                'verbose_name_plural': 'Skills',
            },
        ),
    ]
