# Generated by Django 4.1.5 on 2023-01-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_records'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='img',
            field=models.TextField(max_length=500),
        ),
    ]
