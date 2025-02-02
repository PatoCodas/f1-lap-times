# Generated by Django 5.1.5 on 2025-01-21 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LapTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DurationField()),
                ('date', models.DateField()),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lap_times', to='laptimes.track')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
