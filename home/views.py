from django.shortcuts import render
from django.views import View

from course.models import Course
from category.models import CourseCategory


class HomeView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by('?')[:3]
        categories = CourseCategory.objects.filter(is_child=False)
        new_courses = Course.objects.all()[:4]

        context = {
            'all_courses': all_courses,
            'categories': categories,
            'new_courses': new_courses
        }
        return render(request, 'home/index.html', context)
