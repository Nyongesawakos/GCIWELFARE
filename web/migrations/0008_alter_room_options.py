# Generated by Django 5.1.2 on 2025-01-10 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_rename_client_message_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
