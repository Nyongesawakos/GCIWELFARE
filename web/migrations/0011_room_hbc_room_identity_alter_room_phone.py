# Generated by Django 5.1.2 on 2025-01-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_room_email_room_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='HBC',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='identity',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
