# Generated by Django 5.1.6 on 2025-03-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
