# Generated by Django 4.0.2 on 2022-03-19 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_service_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.garage'),
        ),
    ]