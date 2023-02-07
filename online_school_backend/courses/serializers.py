from .models import Course
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField


class CourseListSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['created_at', 'updated_at']


class CourseCreateSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['created_at', 'updated_at']


class CourseRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['created_at', 'updated_at']
