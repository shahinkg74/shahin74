# Generated by Django 5.0 on 2024-01-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursevideo',
            name='price',
        ),
        migrations.AddField(
            model_name='coursevideo',
            name='is_free',
            field=models.BooleanField(default=False, verbose_name='رایگان'),
        ),
    ]