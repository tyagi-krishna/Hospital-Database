# Generated by Django 4.1.1 on 2022-10-11 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_appointment_endtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='endtime',
            field=models.TextField(default='00'),
        ),
    ]
