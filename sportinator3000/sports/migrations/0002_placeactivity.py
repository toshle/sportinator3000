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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('place', models.ForeignKey(to='sports.Place', to_field='id')),
                ('activity', models.ForeignKey(to='sports.Activity', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
