# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_auto_20140426_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2014, 4, 26, 10, 49, 15, 609933)),
        ),
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.CharField(choices=[('Varna', 'Варна'), ('Sofia', 'София'), ('Plovdiv', 'Пловдив'), ('Stara Zagora', 'Стара Загора'), ('Montana', 'Монтана'), ('Burgas', 'Бургас'), ('Razgrad', 'Разград'), ('Ruse', 'Русе'), ('Jelezna', 'Железна')], max_length=30),
        ),
    ]
