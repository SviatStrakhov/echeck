# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-06 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cashier', '0003_auto_20170806_1143'),
        ('storage', '0002_repository'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=1, max_digits=7, verbose_name='quantity')),
                ('dish', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cashier.Dish')),
            ],
            options={
                'verbose_name': 'Dishcomposition',
                'verbose_name_plural': 'Dishcomposition',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('unit', models.CharField(max_length=256, verbose_name='unit')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='cost')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage.Product')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
            },
        ),
        migrations.AddField(
            model_name='dishcomposition',
            name='ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kitchen.Ingredient'),
        ),
    ]
