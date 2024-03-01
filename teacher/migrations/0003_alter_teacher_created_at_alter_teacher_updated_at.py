# Generated by Django 5.0 on 2024-02-17 10:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_teacher_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default='2023-09-12'),
            preserve_default=False,
        ),
    ]
