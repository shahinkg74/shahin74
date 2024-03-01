# Generated by Django 5.0 on 2024-01-03 20:31

import ckeditor_uploader.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان دوره')),
                ('section', models.CharField(max_length=3, verbose_name='تعداد قسمت ها')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات')),
                ('price', models.PositiveIntegerField(default=0, help_text='به ریال وارد شود', verbose_name='قیمت')),
                ('discount', models.PositiveIntegerField(blank=True, null=True, verbose_name='درصد تخفیف')),
                ('banner', models.ImageField(upload_to='images/course-banner/', verbose_name='بنر')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='اسلاگ')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ساخت')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ آخرین بروزرسانی')),
                ('categories', models.ManyToManyField(related_name='courses', to='category.coursecategory', verbose_name='دسته بندی ها')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='teacher.teacher', verbose_name='آموزگار')),
            ],
            options={
                'verbose_name': 'دوره',
                'verbose_name_plural': 'دوره ها',
            },
        ),
    ]
