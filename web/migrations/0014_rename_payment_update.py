# Generated by Django 5.1.2 on 2025-01-20 08:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_payment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='payment',
            new_name='update',
        ),
    ]
