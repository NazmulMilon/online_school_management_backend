import django_filters
from .models import Course
from django_filters import rest_framework as filters


class CourseFilter(filters.FilterSet):
    course_name = filters.CharFilter(field_name='course_name', lookup_expr='icontains')
    # course_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Course
        # fields = "__all__"
        fields = ['course_code', 'course_name']
