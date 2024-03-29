# Generated by Django 5.0 on 2024-02-17 10:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_alter_coursecategory_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecategory',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='shortvideocategory',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
