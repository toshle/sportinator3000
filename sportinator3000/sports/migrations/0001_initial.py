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
                ('photo_url', models.CharField(blank=True, max_length=300)),
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
                ('city', models.CharField(choices=[('Varna', 'Варна'), ('Sofia', 'София'), ('Plovdiv', 'Пловдив'), ('Stara Zagora', 'Стара Загора'), ('Montana', 'Монтана'), ('Burgas', 'Бургас'), ('Razgrad', 'Разград'), ('Ruse', 'Русе'), ('Jelezna', 'Железна')], max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('photo_url', models.CharField(blank=True, max_length=300)),
                ('video_url', models.CharField(blank=True, max_length=300)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2014, 4, 26, 14, 35, 37, 881497))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('sport', models.ForeignKey(to='sports.Sport', to_field='id')),
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
