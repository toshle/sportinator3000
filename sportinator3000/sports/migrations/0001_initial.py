# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('photo_url', models.CharField(blank=True, max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('city', models.CharField(choices=[('Varna', 'Варна'), ('Sofia', 'София'), ('Plovdiv', 'Пловдив'), ('Stara Zagora', 'Стара Загора'), ('Montana', 'Монтана'), ('Burgas', 'Бургас'), ('Razgrad', 'Разград'), ('Ruse', 'Русе')], max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('photo_url', models.CharField(blank=True, max_length=300)),
                ('video_url', models.CharField(blank=True, max_length=300)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2014, 4, 25, 23, 33, 48, 910795))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('sport', models.ForeignKey(to_field='id', to='sports.Sport')),
                ('name', models.CharField(max_length=200)),
                ('has_trainer', models.BooleanField()),
                ('price', models.FloatField()),
                ('duration', models.IntegerField()),
                ('worktime', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
