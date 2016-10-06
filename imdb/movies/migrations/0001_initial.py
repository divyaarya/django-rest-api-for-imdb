# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(blank=True, null=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(blank=True, null=True, max_length=150)),
                ('imdb_score', models.FloatField(default=0.0)),
                ('popularity_index', models.FloatField(blank=True, null=True)),
                ('director', models.CharField(blank=True, null=True, max_length=100)),
                ('genre', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='genre',
            unique_together=set([('name',)]),
        ),
    ]
