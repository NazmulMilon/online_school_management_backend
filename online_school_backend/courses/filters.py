import django_filters
from .models import Course


class CourseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Course
        fields = ['course_code', 'course_name']
