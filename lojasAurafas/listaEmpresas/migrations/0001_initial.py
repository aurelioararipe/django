# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razao_social', models.CharField(max_length=255)),
                ('proprietario', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
