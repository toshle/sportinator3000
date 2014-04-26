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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo_url', models.CharField(max_length=300, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=50)),
                ('city', models.CharField(choices=[('Varna', 'Варна'), ('Sofia', 'София'), ('Plovdiv', 'Пловдив'), ('Stara Zagora', 'Стара Загора'), ('Montana', 'Монтана'), ('Burgas', 'Бургас'), ('Razgrad', 'Разград'), ('Ruse', 'Русе')], max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('photo_url', models.CharField(max_length=300, blank=True)),
                ('video_url', models.CharField(max_length=300, blank=True)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2014, 4, 26, 6, 8, 1, 819966))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('sport', models.ForeignKey(to_field='id', to='sports.Sport')),
                ('name', models.CharField(max_length=200)),
                ('has_trainer', models.BooleanField(default=True)),
                ('price', models.FloatField()),
                ('duration', models.IntegerField()),
                ('worktime', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
