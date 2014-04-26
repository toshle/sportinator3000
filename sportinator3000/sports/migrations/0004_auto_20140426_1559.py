# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sports', '0003_auto_20140426_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='added_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, to_field='id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2014, 4, 26, 15, 59, 44, 646317)),
        ),
    ]
