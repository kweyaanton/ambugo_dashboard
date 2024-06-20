# Generated by Django 4.2.7 on 2023-11-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_ambulance_booking_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='ambulance_location',
            field=models.CharField(default='Not Provided!', max_length=100),
        ),
        migrations.AddField(
            model_name='ambulance',
            name='driver_name',
            field=models.CharField(default='Not Provided!', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='ambulance',
            name='telephone_number',
            field=models.CharField(default='Not Provided!', max_length=20, unique=True),
        ),
    ]
