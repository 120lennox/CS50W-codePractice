# Generated by Django 5.0.2 on 2024-02-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0002_entries_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
