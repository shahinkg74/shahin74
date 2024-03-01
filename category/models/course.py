from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from category.models import Category


class CourseCategory(Category):
    banner = models.ImageField(
        upload_to='images/category/course-banner/',
        null=True,
        blank=True,
        verbose_name=_("بنر")
    )

    class Meta:
        verbose_name = _("دسته بندی دوره ها")
        verbose_name_plural = _("دسته بندی های دوره ها")

    def get_absolute_url(self):
        return reverse(
            'category:course_category_detail',
            kwargs={'course_category_id': self.id, 'course_category_slug': self.slug}
        )
