# Generated by Django 2.2.6 on 2019-11-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripplanner', '0006_timetabledata_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetabledata',
            name='type',
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('N', 'normal'), ('W', 'weekend'), ('H', 'holiday')], default='N', max_length=1),
        ),
    ]