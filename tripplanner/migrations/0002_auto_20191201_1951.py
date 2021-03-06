# Generated by Django 2.2.6 on 2019-12-01 18:51

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripplanner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='valid_from',
            field=models.DateField(default=datetime.date(2019, 12, 1)),
        ),
        migrations.AlterField(
            model_name='service',
            name='valid_until',
            field=models.DateField(default=datetime.date(2020, 11, 30)),
        ),
        migrations.AlterField(
            model_name='stationorder',
            name='distance',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='stationorder',
            name='station_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to+', to='tripplanner.Station'),
        ),
    ]
