from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from course.models import Course


class CourseCategoryDetailView(View):
    def get(self, request, course_category_id=None, course_category_slug=None):
        courses = Course.objects.filter(
            Q(categories__id=course_category_id) &
            Q(categories__slug=course_category_slug)
        )
        courses_length = len(courses)
        # paginator
        page = request.GET.get('page', 1)
        paginator = Paginator(courses, 8)
        try:
            course_list = paginator.page(page)
        except PageNotAnInteger:
            course_list = paginator.page(1)
        except EmptyPage:
            course_list = paginator.page(paginator.num_pages)
        
        context = {
            'courses': course_list,
            'courses_length': courses_length
        }
        return render(request, 'category/course_category_list.html', context)
