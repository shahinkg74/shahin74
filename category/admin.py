from django.contrib import admin
from .models import CourseCategory, ShortVideoCategory


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_child', 'parent']
    list_filter = ['is_child']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_pre_page = 30


@admin.register(ShortVideoCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_child', 'parent']
    list_filter = ['is_child']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_pre_page = 30
