from category.models import CourseCategory

def course_category(request):
    course_categories = CourseCategory.objects.filter(is_child=False)
    return {
        'course_categories': course_categories
    }
