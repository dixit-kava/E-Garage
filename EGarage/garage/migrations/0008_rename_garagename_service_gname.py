# Generated by Django 4.0.2 on 2022-03-19 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0007_service_garagename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='garagename',
            new_name='gname',
        ),
    ]
