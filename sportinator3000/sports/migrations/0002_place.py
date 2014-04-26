# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('city', models.CharField(choices=[('Varna', 'Варна'), ('Sofia', 'София'), ('Plovdiv', 'Пловдив'), ('Stara Zagora', 'Стара Загора'), ('Montana', 'Монтана'), ('Burgas', 'Бургас'), ('Razgrad', 'Разград'), ('Ruse', 'Русе'), ('Jelezna', 'Железна')], max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('photo_url', models.CharField(blank=True, max_length=300)),
                ('video_url', models.CharField(blank=True, max_length=300)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2014, 4, 26, 15, 48, 12, 99043))),
                ('added_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
