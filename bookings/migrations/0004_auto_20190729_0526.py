# Generated by Django 2.2.3 on 2019-07-29 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_day_reserved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='reserved',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
