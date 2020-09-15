# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-11 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AxfFoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=32)),
                ('typename', models.CharField(max_length=64)),
                ('childtypenames', models.CharField(max_length=128)),
                ('typesort', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_foodtype',
            },
        ),
        migrations.CreateModel(
            name='AxfGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField()),
                ('productimg', models.CharField(max_length=64)),
                ('productname', models.CharField(max_length=64)),
                ('productlongname', models.CharField(max_length=128)),
                ('isxf', models.BooleanField(default=False)),
                ('pmdesc', models.IntegerField()),
                ('specifics', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('marketprice', models.FloatField()),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=128)),
                ('dealerid', models.IntegerField()),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]