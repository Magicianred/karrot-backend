# Generated by Django 3.0.2 on 2020-06-15 12:21
from datetime import datetime

from django.db import migrations
from pytz import utc


def migrate(apps, schema_editor):
    NotificationMeta = apps.get_model('notifications', 'NotificationMeta')

    min_date = datetime.min.replace(tzinfo=utc)

    for meta in NotificationMeta.objects.filter(marked_at__isnull=True):
        meta.marked_at = min_date
        meta.save()


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_add_notification_meta'),
    ]

    operations = [
        migrations.RunPython(migrate, migrations.RunPython.noop, elidable=True),
    ]