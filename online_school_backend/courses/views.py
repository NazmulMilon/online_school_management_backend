from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import UserProfile
from .models import Course, Enrolment
from .serializers import CourseCreateSerializer, CourseRetrieveSerializer, CourseListSerializer, EnrolmentListSerializer, \
    UserRetrieveSerializer, EnrolmentSerializer, EnrollmentSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status


class CourseListAPIView(ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Course.objects.all()
        serializer = CourseListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EnrolmentRetrieveAPIView(ListAPIView):
    serializer_class = EnrolmentListSerializer
    queryset = Enrolment.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        data = dict()
        queryset = Enrolment.objects.filter(user_id=pk).first()

        # course_list = []
        # for item in queryset:
        #     course_data = dict()
        #     course_data["id"] = item.course.id
        #     course_data["course_code"] = item.course.course_code
        #     course_data["course_name"] = item.course.course_name
        #     course_list.append(course_data)
        #
        # data["user"] = pk
        # data["course"] = course_list
        serializer = EnrolmentListSerializer(queryset, many=False)
        # return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EnrollmentCreateAPIView(CreateAPIView):
    queryset = Enrolment.objects.all()
    serializer_class = EnrollmentSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        user = data.get('user', None)
        user_obj = UserProfile.objects.filter(id=user, user_role='STUDENT').first()
        if not user_obj:
            return Response(data={'details': 'User does not found.'}, status=status.HTTP_404_NOT_FOUND)

        course = data.get('course', None)
        course_obj = Course.objects.filter(id=course).exists()
        if not course_obj:
            return Response(data={'details': 'Course ID does not matched. Enter valid course id'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        exist_obj = Enrolment.objects.filter(user_id=user_obj.user, course_id=course_obj.course).exists()
        if exist_obj:
            return Response(data={'details': 'User already have taken the course.'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        enrollment_obj = Enrolment(user_id=user_obj.user_id, course_id=course)
        enrollment_obj.save()
        serializer = EnrollmentSerializer(enrollment_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class EnrollmentListAPIView(ListAPIView):
    queryset = Enrolment.objects.all()
    serializer_class = EnrollmentSerializer

    def get(self, request, *args, **kwargs):
        queryset = Enrolment.objects.all()
        serializer = EnrollmentSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

