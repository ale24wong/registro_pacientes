# Generated by Django 2.0.1 on 2018-05-09 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
