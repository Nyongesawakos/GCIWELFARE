# Generated by Django 5.1.2 on 2024-10-09 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Lastnmame',
            new_name='Lastname',
        ),
    ]
