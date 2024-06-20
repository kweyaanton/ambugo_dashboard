# Generated by Django 4.2.7 on 2023-11-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_remove_ambulance_driver_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='driver_name',
            field=models.CharField(max_length=100, null='False'),
            preserve_default='False',
        ),
        migrations.AlterField(
            model_name='ambulance',
            name='ambulance_location',
            field=models.CharField(max_length=200),
        ),
    ]