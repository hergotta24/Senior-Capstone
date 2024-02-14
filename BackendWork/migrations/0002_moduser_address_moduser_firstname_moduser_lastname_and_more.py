# Generated by Django 5.0.2 on 2024-02-09 02:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendWork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moduser',
            name='address',
            field=models.CharField(blank=True, max_length=72),
        ),
        migrations.AddField(
            model_name='moduser',
            name='firstName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='moduser',
            name='lastName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='moduser',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='moduser',
            name='registrationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='moduser',
            name='password',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]