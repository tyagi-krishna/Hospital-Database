# Generated by Django 4.1.1 on 2022-10-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('1', 'Mental Health'), ('2', 'Heart Diseases'), ('3', 'Covid19'), ('4', 'Immunization')], default='1', max_length=2),
        ),
    ]
