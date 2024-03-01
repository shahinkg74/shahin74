from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'bio']
    list_per_page = 30
