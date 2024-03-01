from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'price']
    list_fielter = ['created_at', 'updated_at']
    search_fields = ['title', 'description']
    raw_id_fields = ['categories', 'teacher']
    prepopulated_fields = {'slug': ('title',)}
    list_pre_page = 30
