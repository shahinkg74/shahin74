# Generated by Django 5.0 on 2024-02-17 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_shortvideocategory_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecategory',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 2, 17, 10, 39, 30, 728834, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='coursecategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default='2024-10-3'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shortvideocategory',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 2, 17, 10, 39, 30, 728834, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='shortvideocategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default='2024-02-09'),
            preserve_default=False,
        ),
    ]
