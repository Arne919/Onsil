# Generated by Django 4.2.16 on 2024-09-23 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garages', '0002_garage_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='garage',
            name='name',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]