# Generated by Django 2.0.1 on 2018-05-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=100)),
            ],
        ),
    ]