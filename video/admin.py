from django.contrib import admin
from .models import CourseVideo, ShortVideo


@admin.register(CourseVideo)
class CourseVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'get_courses']
    list_fielter = ['created_at', 'updated_at', 'courses']
    search_fields = ['title', 'description']
    raw_id_fields = ['teacher', 'courses']
    prepopulated_fields = {'slug': ('title',)}
    list_pre_page = 30

    def get_courses(self, obj):
        return " | ".join([course.title for course in obj.courses.all()])


@admin.register(ShortVideo)
class ShortVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'get_categories']
    list_fielter = ['created_at', 'updated_at']
    search_fields = ['title', 'description']
    raw_id_fields = ['teacher', 'categories']
    prepopulated_fields = {'slug': ('title',)}
    list_pre_page = 30

    def get_categories(self, obj):
        return " | ".join([category.title for category in obj.categories.all()])
