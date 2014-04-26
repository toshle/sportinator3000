# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_placeactivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2014, 4, 26, 17, 11, 36, 759329)),
        ),
    ]
