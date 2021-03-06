# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-28 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='carousel')),
                ('order', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassiFication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classimg', models.ImageField(upload_to='class')),
                ('typename', models.CharField(max_length=16)),
                ('childtypenames', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distname', models.CharField(max_length=30)),
                ('distimg', models.ImageField(upload_to='dist')),
                ('describe', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsname', models.CharField(max_length=50, unique=True)),
                ('goodsimg', models.ImageField(upload_to='goods')),
                ('price', models.FloatField()),
                ('norms', models.CharField(max_length=20)),
                ('abstract', models.CharField(max_length=100)),
                ('commodity', models.TextField()),
                ('classify', models.CharField(max_length=16)),
                ('subclass', models.CharField(max_length=16)),
                ('is_recommend', models.BooleanField(default=0)),
                ('popularity', models.IntegerField(default=0)),
                ('class_f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ClassiFication')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('distribution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Distribution')),
            ],
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattname', models.CharField(max_length=30)),
                ('pattimg', models.ImageField(upload_to='pattern')),
                ('describe', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=1)),
                ('is_select', models.BooleanField(default=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Static',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='carousel')),
                ('order', models.IntegerField(unique=True)),
                ('classi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ClassiFication')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('is_root', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=256)),
                ('out_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressee', models.CharField(max_length=20)),
                ('site', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User')),
            ],
        ),
        migrations.AddField(
            model_name='shopping',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='pattern',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Pattern'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='classi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ClassiFication'),
        ),
    ]
