# Generated by Django 4.0.2 on 2022-03-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0011_remove_service_mapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='services',
            field=models.CharField(max_length=1000),
        ),
    ]
