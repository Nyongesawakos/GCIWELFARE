# Generated by Django 5.1.2 on 2025-01-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_room_hbc_room_identity_alter_room_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='identity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
