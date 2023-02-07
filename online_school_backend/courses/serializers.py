from django.contrib.auth.models import User
from .models import Course, Enrolment
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


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class EnrolmentSerializer(ModelSerializer):
    class Meta:
        model = Enrolment
        exclude = ['created_at', 'updated_at']


class EnrolmentListSerializer(ModelSerializer):
    user = SerializerMethodField()
    course = SerializerMethodField()

    def get_course(self, instance):
        course_id_list = []
        enrol_qs = Enrolment.objects.filter(user=instance.user).values("course")
        for item in enrol_qs:
            if item["course"] and item["course"] not in course_id_list:
                course_id_list.append(item["course"])
        course_queryset = Course.objects.filter(pk__in=course_id_list)
        return CourseListSerializer(course_queryset, many=True).data

    def get_user(self, instance):
        return instance.user.id

    class Meta:
        model = Enrolment
        exclude = ['id', 'created_at', 'updated_at']


class UserRetrieveSerializer(ModelSerializer):
    course = SerializerMethodField()

    def get_course(self, instance):
        queryset = Course.objects.filter(id=instance.course_id)
        return CourseListSerializer(queryset, many=True).data

    class Meta:
        model = Enrolment
        exclude = ['created_at', 'updated_at']


class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrolment
        exclude = ['created_at', 'updated_at']