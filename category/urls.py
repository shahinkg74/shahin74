from django.urls import path
from .views import CourseCategoryDetailView

app_name = 'category'
urlpatterns = [
    path(
        '<int:course_category_id>/<str:course_category_slug>/courses/',
        CourseCategoryDetailView.as_view(),
        name='course_category_detail'
    ),
]
