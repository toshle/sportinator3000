# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('place', models.ForeignKey(to_field='id', to='sports.Place')),
                ('activity', models.ForeignKey(to_field='id', to='sports.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
