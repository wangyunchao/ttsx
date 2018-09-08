# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-28 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_goods_is_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=1)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Goods')),
            ],
            options={
                'db_table': 'order_goods',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_goods',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Order'),
        ),
    ]