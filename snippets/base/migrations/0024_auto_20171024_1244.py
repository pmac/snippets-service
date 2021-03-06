# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 12:44
from __future__ import unicode_literals
import uuid

from django.db import migrations


def gen_uuid(apps, schema_editor):
    for model in [apps.get_model('base', 'Snippet'), apps.get_model('base', 'JSONSnippet')]:
        for row in model.objects.all():
            row.uuid = uuid.uuid4()
            row.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_auto_20171024_1244'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
